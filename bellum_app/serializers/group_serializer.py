from rest_framework import  serializers
from bellum_app.models import Group
from datetime import datetime


class My_GroupSerializer(serializers.ModelSerializer):


    class Meta:
        model = Group
        fields = ('name','description')


    def create(self, validated_data):
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
