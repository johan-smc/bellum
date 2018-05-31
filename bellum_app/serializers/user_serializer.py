from rest_framework import  serializers
from bellum_app.models import My_User,Role
from django.contrib.auth.models import User
from hashlib import  sha3_384
from bellum.settings import FILE_ROOT
import os



class My_UserSerializer(serializers.ModelSerializer):
    #user_django = serializers.ReadOnlyField(required=False)
    role = serializers.Field(required=False,write_only=True)
    logs = serializers.CharField(required=False)
    password_change = serializers.ReadOnlyField(required=False)
    class Meta:
        model = My_User
        fields = '__all__'



    def create(self, validated_data,user):
        #data = validated_data.pop('role')
        data = 2;
        role = Role.objects.get(pk=data)
        validated_data['role'] = role
        path = FILE_ROOT+'/logs/'+user.username+'log'
        validated_data['logs'] = path
        open(path, 'w')
        return My_User.objects.create(user_django=user,**validated_data)



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    my_user = My_UserSerializer(required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'my_user')

    def create(self, validated_data):
        profile_data = validated_data.pop('my_user')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        my_user = My_UserSerializer(data=profile_data)
        if my_user.is_valid():
            my_user.create(profile_data,user)

        return user


    def INodeSerializer(self):
        pass