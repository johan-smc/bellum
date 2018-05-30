from django.shortcuts import render

import datetime

from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from bellum_app.models import Group

from bellum_app.api import user_service, file_service
from bellum_app.models import User, INode
from bellum_app.serializers.file_serializer import File_Serializer, Folder_Serializer

from bellum_app.serializers.user_serializer import UserSerializer
from bellum_app.serializers.group_serializer import My_GroupSerializer
from bellum_app.serializers.user_file_serializer import UserFileSerializer
from bellum_app.serializers.group_file_serializer import GroupFileSerializer
from bellum_app.api import group_service


# Create your views here.


class ObtainExpiringAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])

            if not created:
                token.created = datetime.datetime.utcnow()
                token.save()

            response_data = {'token': token.key}
            return Response(

                response_data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class GroupViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
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

    def get(self, request):
        group_serializer = My_GroupSerializer(
            group_service.get_groups(),
            many=True
        )
        print(group_serializer.data)
        return Response(
            group_serializer.data,
            status=status.HTTP_200_OK
        )

    def removeG(self, request):
        print("AAAaAAaA", request.data)
        group_service.remove(self, request.data)
        txt = "grupo con id %s" % (request["id"])
        return Response(
            "grupo borrado",
            status=status.HTTP_202_ACCEPTED

        )

    def usrGroup(self, request):
        if (group_service.usrJoin(self, request.data)):
            return Response(
                "usr asociado",
                status=status.HTTP_202_ACCEPTED
            )
        return Response(
            "USR no valido",
            status=status.HTTP_404_NOT_FOUND
        )

    def unUsrgroup(self, request):
        if (group_service.usrUnJoin(self, request.data)):
            return Response(
                "usr disociado",
                status=status.HTTP_202_ACCEPTED
            )
        return Response(
            "USR no valido",
            status=status.HTTP_404_NOT_FOUND
        )

    def update(self, request):
        print(request.data["id"])
        instance = Group.objects.get(id=request.data["id"])
        group_Serializer = My_GroupSerializer(instance, data=request.data)
        group_Serializer.update(instance, request.data)
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


class FileViewSet(viewsets.ViewSet):

    def create(self, request):
        request.POST._mutable = True
        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]

        request.data['owner'] = user_service.get_pk(token)
        file_serializer = File_Serializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            # file_serializer.create(request.data)
            return Response(
                file_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            file_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request):
        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        #######
        user_id = request.data['owner'] = user_service.get_pk(token)
        file_id = request.data['file_id']
        if file_service.get_permissions(user_id,file_id) < 2 :
            return Response(
                "Insufficient permissions",
                status=status.HTTP_400_BAD_REQUEST
            )
        #######

        if file_service.delete(file_id):
            return Response(
                "Deleted ok",
                status=status.HTTP_200_OK
            )
        return Response(
            "Not deleted",
            status=status.HTTP_400_BAD_REQUEST
        )

    def update_file(self, request):
        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        request.data['owner'] = user_service.get_pk(token)

        #####
        user_id = request.data['owner']
        file_id = request.data['id']
        if file_service.get_permissions(user_id,file_id) < 2 :
            return Response(
                "Insufficient permissions",
                status=status.HTTP_400_BAD_REQUEST
            )
        ###

        instance = INode.objects.get(id=request.data['id'])
        file_serializer = File_Serializer(instance, data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            # file_serializer.create(request.data)
            return Response(
                file_serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            file_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def create_folder(self, request):
        request.POST._mutable = True
        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]

        request.data['owner'] = user_service.get_pk(token);
        folder_serializer = Folder_Serializer(data=request.data)
        if folder_serializer.is_valid():
            folder_serializer.save()
            # file_serializer.create(request.data)
            return Response(
                folder_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            folder_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    def relation_user(self, request):
        user_file_serializer = UserFileSerializer(data=request.data)
        #######
        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        user_id =  user_service.get_pk(token)
        file_id = request.data['inode']
        if file_service.get_permissions(user_id, file_id) < 2:
            return Response(
                "Insufficient permissions",
                status=status.HTTP_400_BAD_REQUEST
            )
        #######

        if user_file_serializer.is_valid():
            user_file_serializer.create(request.data)
            return Response(
                user_file_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            user_file_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def relation_group(self, request):
        group_file_serializer = GroupFileSerializer(data=request.data)

        #######
        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        user_id = user_service.get_pk(token)
        file_id = request.data['inode']
        if file_service.get_permissions(user_id, file_id) < 2:
            return Response(
                "Insufficient permissions",
                status=status.HTTP_400_BAD_REQUEST
            )
        #######

        if group_file_serializer.is_valid():
            group_file_serializer.create(request.data)
            return Response(
                group_file_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            group_file_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete_user(self,request):
        user_id = request.data['user']
        inode_id = request.data['inode']
        if file_service.delete_user(user_id, inode_id):
            return Response(
                "ok Delete",
                status=status.HTTP_201_CREATED
            )
        return Response(
            "wrong params",
            status=status.HTTP_400_BAD_REQUEST
        )
    def delete_group(self, request):
        group_id = request.data['group']
        inode_id = request.data['inode']
        if file_service.delete_group(group_id, inode_id):
            return Response(
                "ok Delete",
                status=status.HTTP_201_CREATED
            )
        return Response(
            "wrong params",
            status=status.HTTP_400_BAD_REQUEST
        )

    def get_inodes(self, request):
        type = request.data['type']
        if type == 'DIR':
            resp = file_service.get_all_inodes(request.data['father'])
            folder_serializer = Folder_Serializer(
                resp,
                many=True
            )
            return Response(
                folder_serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return  Response(
                "Not a directory",
                status=status.HTTP_400_BAD_REQUEST
            )


get_users = UserViewSet.as_view(dict(get='get'))
register_group = GroupViewSet.as_view(dict(post='create', put='update'))
get_groups = GroupViewSet.as_view(dict(get='get'))
del_group = GroupViewSet.as_view(dict(delete='removeG'))
usr_to_group = GroupViewSet.as_view(dict(post='usrGroup', delete="unUsrgroup"))
obtain_expiring_auth_token = ObtainExpiringAuthToken.as_view()
upload_file = FileViewSet.as_view(dict(post='create'))
del_file = FileViewSet.as_view(dict(delete='delete'))
create_folder = FileViewSet.as_view(dict(post='create_folder'))
update_file = FileViewSet.as_view(dict(put='update_file'))
inode_user = FileViewSet.as_view(dict(post='relation_user', delete='delete_user'))
inode_group = FileViewSet.as_view(dict(post='relation_group', delete='delete_group'))
get_inodes = FileViewSet.as_view(dict(post='get_inodes'))
register = UserViewSet.as_view(dict(post='create'))


