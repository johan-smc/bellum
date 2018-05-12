from django.shortcuts import render


from rest_framework.response import Response
from rest_framework import status, viewsets

from bellum_app.serializers.user_serializer import UserSerializer
# Create your views here.


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


register =UserViewSet.as_view(dict(post='create'))