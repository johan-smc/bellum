from django.shortcuts import render

import datetime

from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from bellum_app.models import Group

from bellum_app.api import  user_service
from bellum_app.models import User


from bellum_app.serializers.user_serializer import UserSerializer
from bellum_app.serializers.group_serializer import My_GroupSerializer
from bellum_app.api import group_service
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

class GroupViewSet(viewsets.ViewSet):
    def create(self,request, *args, **kwargs):
        groups_serializer = My_GroupSerializer(data=request.data)

        if groups_serializer.is_valid():
            groups_serializer.create(request.data)
            return Response(
                groups_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
                groups_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
        )

    def get(self,request):
        group_serializer = My_GroupSerializer(
            group_service.get_groups(),
            many=True
        )
        print(group_serializer.data)
        return Response(
                group_serializer.data,
                status=status.HTTP_200_OK
        )
    def removeG(self,request):
        print("AAAaAAaA",request.data)
        group_service.remove(self,request.data)
        txt="grupo con id %s" %(request["id"])
        return Response(
            "grupo borrado",
            status=status.HTTP_202_ACCEPTED

        )
    def usrGroup(self,request):
        if(group_service.usrJoin(self,request.data)):
            return Response(
                "usr asociado",
                status=status.HTTP_202_ACCEPTED
            )
        return Response(
            "USR no valido",
            status=status.HTTP_404_NOT_FOUND
        )
    def unUsrgroup(self,request):
        if (group_service.usrUnJoin(self, request.data)):
            return Response(
                "usr disociado",
                status=status.HTTP_202_ACCEPTED
            )
        return Response(
            "USR no valido",
            status=status.HTTP_404_NOT_FOUND
        )
    def update(self,request):
        print(request.data["id"])
        instance = Group.objects.get(id=request.data["id"])
        group_Serializer=My_GroupSerializer(instance,data=request.data)
        group_Serializer.update(instance,request.data)
        return Response(
            status=status.HTTP_202_ACCEPTED
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


register =UserViewSet.as_view(dict(post='create'))

get_users = UserViewSet.as_view(dict(get='get'))
register_group = GroupViewSet.as_view(dict(post='create',put='update'))
get_groups = GroupViewSet.as_view(dict(get='get'))
del_group = GroupViewSet.as_view(dict(delete='removeG'))
usr_to_group = GroupViewSet.as_view(dict(post='usrGroup',delete="unUsrgroup"))

obtain_expiring_auth_token = ObtainExpiringAuthToken.as_view()