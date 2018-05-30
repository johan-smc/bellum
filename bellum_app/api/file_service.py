from bellum_app.models import INode
import os

def delete(file_id):
    try:
        file = INode.objects.get(id=file_id)
    except INode.DoesNotExist:
        return False
    os.remove(file.file.path)
    file.delete()
    return True

def get_all_inodes(id):
    try:

        lista = INode.objects.filter(father=id)
        return lista
    except INode.DoesNotExist:
        return None
