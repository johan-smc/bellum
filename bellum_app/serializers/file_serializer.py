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
from bellum_app.api.os_service import encrypt_file
import os


class File_Serializer(serializers.ModelSerializer):
    type = serializers.CharField(required=False, default="FILE")
    file = serializers.FileField(write_only=True)
    class Meta:
        model = INode
        fields = ('name','type','password','file','owner','father')

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
        return file


    def update(self, instance, validated_data):
        try:
            os.remove(instance.file.path)
        except OSError:
            print("error")
        instance.file = validated_data.get('file', instance.file)
        filehash = instance.file.__str__().encode()
        filehash = sha3_384(filehash)
        aux = instance.last_user_mod
        instance.last_user_mod = instance.owner
        instance.owner = aux
        instance.update_date()
        instance.last_hash = filehash.hexdigest()
        instance.save()
        return instance


class Folder_Serializer(serializers.ModelSerializer):
    type = serializers.CharField(required=False,default="DIR")
    class Meta:
        model = INode
        fields = ('name','type','password','owner','father')

    def create(self, validated_data):

        return INode.objects.create( **validated_data)