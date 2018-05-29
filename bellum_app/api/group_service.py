from bellum_app.models import Group

def get_groups():
    print(Group.objects.all())
    return Group.objects.all()

def remove(self,data):
    instance = Group.objects.get(id=data["id"])
    instance.delete()

def usrJoin(self,data):

    instance = Group.objects.get(id=data["idGroup"])
    return instance.usrJoin(data)

def usrUnJoin(self,data):
    instance = Group.objects.get(id=data["idGroup"])
    return instance.usrUnJoin(data)
