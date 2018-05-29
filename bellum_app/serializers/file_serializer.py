from rest_framework import  serializers

from bellum.settings import FILE_ROOT
from bellum_app.api.user_service import get_myuser
from bellum_app.models import INode,My_User
from django.contrib.auth.models import User
from hashlib import  sha3_384



class File_Serializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)
    class Meta:
        model = INode
        fields = ('name','type','password','file','owner')

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
        return INode.objects.create( **validated_data)

