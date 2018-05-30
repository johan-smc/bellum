from rest_framework import  serializers
from bellum_app.models import Group_Inode
from bellum_app.api import file_service,group_service

class GroupFileSerializer(serializers.ModelSerializer):
    group = serializers.ReadOnlyField(source='user.id')
    inode = serializers.ReadOnlyField(source='inode.id')

    class Meta:
        model = Group_Inode
        fields = ('group','inode','permission')

    def create(self, validated_data):
        validated_data['inode'] = file_service.get_inode(validated_data['inode'])
        validated_data['group'] = group_service.get_group(validated_data['group'])

        return Group_Inode.objects.create( **validated_data)