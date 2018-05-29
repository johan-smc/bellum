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