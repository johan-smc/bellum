import asyncio

from rest_framework import  serializers
from django.db import models
from datetime import  datetime,timedelta
from bellum.settings import FILE_ROOT
from bellum_app.api.user_service import get_myuser
from bellum_app.models import INode,My_User
from datetime import datetime
from django.contrib.auth.models import User
from hashlib import  sha3_384
from bellum_app.api import os_service
from bellum_app.serializers import user_file_serializer, user_serializer
import os
from simplecrypt import encrypt, decrypt



class File_Serializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    type = serializers.CharField(required=False, default="FILE")
    file = serializers.FileField(write_only=True)
    password = serializers.Field(write_only=True,required=False)
    last_hash = serializers.ReadOnlyField()
    last_user_mod = user_serializer.My_UserSerializer(read_only=True)
    user_inode_set = user_file_serializer.UserFileSerializer(read_only=True,many=True)
    owner = user_serializer.My_UserSerializer(required=False)
    class Meta:
        model = INode
        fields = ('id','name','type','password','file','owner','father','last_hash','user_inode_set','last_user_mod')

    def create(self, validated_data):
        print(validated_data)
        ''' 
        id = validated_data.pop('owner')[0]
        print("voy a crear")
        print(id)
        #my_user = get_myuser(id)
        print(validated_data)
        my_user = My_User.objects.get(id=id)
        '''
        file = INode.objects.create( **validated_data)
        print(file.password)
        os_service.encrypt_file(file.file.path,file.password)
        os_service.write_in_log("Create file the user: "+file.owner.user_django.username+ "\n", file.owner.id)
        return file


    def update(self, instance, validated_data):
        '''
        try:
            os.remove(instance.file.path)
        except OSError:
            print("error")
        '''
        print("------------")
        print(instance)
        print(validated_data)
        instance.file = validated_data.get('file', instance.file)
        instance.name = validated_data.get('name', instance.name)
        instance.owner = validated_data.get('owner', instance.owner)
        filehash = instance.file.__str__().encode()
        filehash = sha3_384(filehash)
        instance.update_date()
        instance.last_hash = filehash.hexdigest()
        instance.save()

        os_service.write_in_log("update file the user: " + instance.owner.user_django.username, instance.owner.id)
        return instance


class Folder_Serializer(serializers.ModelSerializer):
    last_hash = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    type = serializers.CharField(required=False,default="DIR")
    password = serializers.Field(write_only=True,required=False)
    user_inode_set = user_file_serializer.UserFileSerializer(read_only=True, many=True)
    last_user_mod = user_serializer.My_UserSerializer(read_only=True)
    class Meta:
        model = INode
        fields = ('id','name','type','password','owner','father','last_hash','user_inode_set','last_user_mod')

    def create(self, validated_data):
        file = INode.objects.create( **validated_data)
        os_service.write_in_log("Create folder the user: " + file.owner.user_django.username+ "\n", file.owner.id)
        return file