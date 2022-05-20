from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
from .serializers import DoctorSerializer
from .models import Doctors


class Registration(APIView):
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        # if serializer.is_valid():
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        # else:
        # serializer = ({
        #     "status": 0,
        #     "errors": serializer.errors
        # })
        # return Response(serializer, status=status.HTTP_404_NOT_FOUND)
        # return Response(serializer)


class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        print(password)
        user = Doctors.objects.filter(email=email).first()

        print(user.check_password(password))
        # serializer = DoctorSerializer(user).data
        if user is None:
            raise AuthenticationFailed('user not found')

        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')

        # for tokens
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret',
                           algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = Doctors.objects.filter(id=payload['id']).first()
        serializer = DoctorSerializer(user)
        return Response(serializer.data)


class Logout(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
