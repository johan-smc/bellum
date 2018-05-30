from rest_framework import  serializers
from bellum_app.models import User_Inode
from bellum_app.api import file_service,user_service

class UserFileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    inode = serializers.ReadOnlyField(source='inode.id')

    class Meta:
        model = User_Inode
        fields = ('user','inode','permission')

    def create(self, validated_data):
        validated_data['inode'] = file_service.get_inode(validated_data['inode'])
        validated_data['user'] = user_service.get_myuser(validated_data['user'])

        return User_Inode.objects.create( **validated_data)