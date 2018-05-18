from rest_framework import  serializers
from bellum_app.models import User,Role

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = '__all__'



    def create(self, validated_data):
        data = validated_data.pop('role')
        role = Role.objects.get(pk=data)
        validated_data['role'] = role;
        return User.objects.create(**validated_data)