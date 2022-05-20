from rest_framework.response import Response
# permission_classes, authentication_classes,
# from rest_framework.decorators import api_view
# from rest_framework import serializers, status
# from user import myjwt
from .serializers import DoctorSerializer
from .models import Doctors
# from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime

# Create your views here.


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
        user = Doctors.objects.filter(email=email).first()

        print(user.check_password(request.data['password']))
        # serializer = DoctorSerializer(user).data
        if user is None:
            raise AuthenticationFailed('user not found')

        # if not user.check_password(password):
        #     raise AuthenticationFailed('incorrect password')

        # for tokens
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        #    algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
        # return Response({
        #     'jwt': token
        # })
