from django.db import models
from hashlib import  sha3_384
from Crypto.PublicKey import RSA
from datetime import  datetime,timedelta
import pytz

from django.contrib.auth.models import User
# token
from rest_framework.authentication import  TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from rest_framework import exceptions

# Create your models here.

TYPE_CHOICES = (
    ('DIR', 'Directory'),
    ('FILE', 'File')
)
ROLE_CHOICES = (
    ('ADM','Administrator'),
    ('USR', 'User')
)

class Role(models.Model):
    name = models.CharField(max_length=4,choices=ROLE_CHOICES)
    permission = models.IntegerField(default=0)



class My_User(models.Model):
    creation_field = models.DateTimeField(default=datetime.now, blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    modification_time = models.DateTimeField(default=datetime.now, blank=True)
    password_change = models.DateTimeField(default=datetime.now, blank=True)
    private_key = models.CharField(max_length=300, unique=True, blank=True)
    public_key = models.CharField(max_length=200, unique=True, blank=True)
    logs = models.CharField(max_length=300)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    user_django = models.OneToOneField(User, on_delete=models.CASCADE)
    #user_name = models.CharField(max_length=25, unique=True)
    #password = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        '''
        #hash password
        password = self.password.encode()
        hash = sha3_384(password)
        self.password = hash.hexdigest()
        '''
        #generate private and public key
        key = RSA.generate(2048) # TODO - verify params
        self.private_key = key
        self.public_key = key.publickey()

        super(My_User, self).save(*args,**kwargs)

class Group(models.Model):
    name = models.CharField(max_length=100)
    creation_field = models.DateTimeField()
    modification_time = models.DateTimeField()
    description = models.CharField(max_length=500)
    users = models.ManyToManyField(
        'My_User',
        related_name='groups'
    )


class INode(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=300)
    type = models.CharField(max_length=5,choices=TYPE_CHOICES)
    creation_field = models.DateTimeField()
    modification_time = models.DateTimeField()
    permission = models.IntegerField(default=0)
    password = models.CharField(max_length=400)
    last_hash = models.CharField(max_length=400)
    owner = models.OneToOneField(
        My_User,
        on_delete=models.CASCADE
    )
    users = models.ManyToManyField(
        'My_User',
        related_name='inodes',
        through='User_Inode'
    )
    groups = models.ManyToManyField(
        'Group',
        related_name='inodes',
        through='Group_Inode'
    )

class User_Inode(models.Model):
    user = models.ForeignKey(My_User, on_delete=models.CASCADE)
    inode = models.ForeignKey(INode, on_delete=models.CASCADE)
    permission = models.IntegerField()

class Group_Inode(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    inode = models.ForeignKey(INode, on_delete=models.CASCADE)
    permission = models.IntegerField()

class ExpiringTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        print(Token.objects.get(key=key))
        print(self.model)
        print(key)
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid Token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or delete')

        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        if token.created < utc_now - timedelta(hours=24):
            raise  exceptions.AuthenticationFailed('Token has expired')

        return token.user, token
