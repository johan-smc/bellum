from django.db import models

# Create your models here.

TYPE_CHOICES = (
    ('DIR', 'Directory'),
    ('FILE', 'File')
)
ROLE_CHOICES = (
    ('ADM','Administrator'),
    ('USR' , 'User')
)

class Role(models.Model):
    name = models.CharField(max_length=4,choices=ROLE_CHOICES)
    permission = models.IntegerField(default=0)


class Log(models.Model):
    path = models.CharField(max_length=300)


class Group(models.Model):
    name = models.CharField(max_length=100)
    creation_field = models.DateTimeField()
    modification_time = models.DateTimeField()
    description = models.CharField(max_length=500)


class User(models.Model):
    creation_field = models.DateTimeField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    user_name = models.CharField(max_length=25, unique=True)
    modification_time = models.DateTimeField()
    password = models.CharField(max_length=100)
    password_change = models.DateTimeField()
    private_key = models.CharField(max_length=300, unique=True)
    public_key = models.CharField(max_length=200, unique=True)
    role = models.OneToOneField(Role)
    logs = models.OneToOneField(Log)
    groups = models.ManyToManyField(
        Group,
        related_name='users'
    )


class Object(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=300)
    type = models.CharField(max_length=5,choices=TYPE_CHOICES)
    creation_field = models.DateTimeField()
    modification_time = models.DateTimeField()
    permission = models.IntegerField(default=0)
    password = models.CharField(max_length=400)
    last_hash = models.CharField(max_length=400)
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    users = models.ManyToManyField(
        User,
        related_name='objects',
        through='User_Object'
    )
    groups = models.ManyToManyField(
        Group,
        related_name='objects',
        through='Group_Object'
    )

class User_Object(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    permission = models.IntegerField()

class Group_Object(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    permission = models.IntegerField()

