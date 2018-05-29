from django.shortcuts import render

import datetime

from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny


from bellum_app.models import User


from bellum_app.serializers.user_serializer import UserSerializer
# Create your views here.


class ObtainExpiringAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.authenticate():


            user = serializer.get_user()
            print(user)
            token, created = Token.objects.get_or_create(user=user)

            utc_now = datetime.datetime.utcnow()
            if not created and token.created < utc_now - datetime.timedelta(hours=24):
                token.delete()
                token = Token.objects.create(user=serializer.object(['user']))
                token.created = datetime.datetime.utcnow()
                token.save()

            response_data = {'token': token.key}
            return Response(
              response_data,
             status = status.HTTP_200_OK
            )
        return Response(
                "Wrong password",
                status = status.HTTP_400_BAD_REQUEST
        )




class UserViewSet(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):

        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.create(user_serializer.data)
            return Response(
                user_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            user_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


register =UserViewSet.as_view(dict(post='create'))
obtain_expiring_auth_token = ObtainExpiringAuthToken.as_view()