from bellum_app.api import user_service, group_service,os_service
from bellum_app.models import INode,User_Inode,Group_Inode
import os

def delete(file_id,user_id):
    try:
        file = INode.objects.get(id=file_id)
    except INode.DoesNotExist:
        return False
    os.remove(file.file.path)
    user = user_service.get_myuser(user_id)
    os_service.write_in_log("Delete file the user: "+user.user_django.username, file.logs )
    file.delete()

    return True



def get_inode(file_id):
    return INode.objects.get(id=file_id)

def delete_user(user,inode):
    try:
        users = User_Inode.objects.filter(user=user,inode=inode)
        for user in users:
            user.delete()

    except User_Inode.DoesNotExist:
        return False

    return True

def delete_group(group,inode):
    try:
        print(group)
        print(inode)
        groups = Group_Inode.objects.filter(group=group, inode=inode)
        for group in groups:
            group.delete()
    except INode.DoesNotExist :
        return False

    return True



def get_permissions(user_id,file_id):

    file = get_inode(file_id)
    permissions = 0
    if file.owner.id == user_id:
        permissions = 3

    user_inode = User_Inode.objects.filter(user=user_id,inode=file_id)
    if user_inode:
        user_inode = user_inode[0]
        permissions = max(permissions,user_inode.permission)

    groups = user_service.get_myuser(user_id).groups.all()
    for group in groups:
        group_inode = Group_Inode.objects.filter(group=group.id, inode=file_id)
        if group_inode:
            group_inode = group_inode[0]
            permissions = max(permissions, group_inode.permission)

    return permissions

def get_all_inodes(id,id_user):
    try:
        lista = INode.objects.filter(father=id, owner= id_user)
        return lista
    except INode.DoesNotExist:
        return None
