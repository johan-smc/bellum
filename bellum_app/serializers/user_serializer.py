from rest_framework import  serializers
from bellum_app.models import User,Role
from hashlib import  sha3_384

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

    def authenticate(self):
        user = User.objects.get(user_name=self.initial_data['user_name'])
        hash_temp = sha3_384(self.initial_data['password'].encode()).hexdigest()
        if user.password == hash_temp :
            return True
        return False

    def get_user(self):
        user = User.objects.get(user_name=self.initial_data['user_name'])
        print(user)
        return user