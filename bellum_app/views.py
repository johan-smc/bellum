from django.shortcuts import render

import datetime

from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny


from bellum_app.api import  user_service, file_service
from bellum_app.models import User
from bellum_app.serializers.file_serializer import File_Serializer

from bellum_app.serializers.user_serializer import UserSerializer
# Create your views here.


class ObtainExpiringAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():


            token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])

            if not created :
                token.created = datetime.datetime.utcnow()
                token.save()

            response_data = {'token': token.key}
            return Response(
              response_data,
             status = status.HTTP_200_OK
            )
        return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
        )




class UserViewSet(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.create(request.data)
            return Response(
                user_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            user_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request):
        return Response(
            "ok funciono creo",
            status=status.HTTP_200_OK
        )

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class FileViewSet(viewsets.ViewSet):

    def create(self, request):
        request.POST._mutable = True
        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]

        request.data['owner'] = user_service.get_pk(token);
        file_serializer = File_Serializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            #file_serializer.create(request.data)
            return Response(
                file_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            file_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete (self,request):
        if file_service.delete(request.data['file_id']) :
            return Response(
                "Deleted ok",
                status=status.HTTP_200_OK
            )
        return Response(
            "Not deleted",
            status=status.HTTP_400_BAD_REQUEST
        )


register =UserViewSet.as_view(dict(post='create'))
get_users = UserViewSet.as_view(dict(get='get'))
obtain_expiring_auth_token = ObtainExpiringAuthToken.as_view()
upload_file = FileViewSet.as_view(dict(post='create'))
del_file =  FileViewSet.as_view(dict(delete='delete'))