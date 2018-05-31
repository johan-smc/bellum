from rest_framework import  serializers
from bellum_app.models import Group
from datetime import datetime

from bellum_app.api import  user_service


class My_GroupSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Group
        fields = ('name','description' , 'id' , 'owner')


    def create(self, validated_data):
        validated_data['owner'] = user_service.get_myuser(validated_data['owner'])
        groupAux= Group.objects.create(**validated_data)
        print("Creando grupo")
        print(groupAux.id)
        return groupAux

    def update(self, instance, validated_data):
        print("hallloooo")
        instance.name =validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.modification_time= datetime.now
        instance.save()
