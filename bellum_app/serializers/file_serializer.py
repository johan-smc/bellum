from rest_framework import  serializers

from bellum_app.api.user_service import get_myuser
from bellum_app.models import INode,My_User
from django.contrib.auth.models import User
from hashlib import  sha3_384



class File_Serializer(serializers.ModelSerializer):
    class Meta:
        model = INode
        fields = '__all__'

    def create(self, validated_data):
        id = validated_data.pop('owner')[0]
        print(id)
        #my_user = get_myuser(id)
        my_user = My_User.objects.get(id=id)
        return INode.objects.create(owner= my_user, **validated_data)

