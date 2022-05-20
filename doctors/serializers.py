from rest_framework import serializers
from .models import Doctors


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        # fields = "__all__"
        fields = ['id', 'name', 'email', 'password']

        # to unreturned password
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }

    # to hash password
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # password = validated_data['password']
        instance = self.Meta.model(**validated_data)
        if password is not None:
            # this fun is created by Django
            instance.set_password(instance.password)
        instance.save()
        return instance
