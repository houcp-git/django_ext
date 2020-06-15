from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager,BaseUserManager,PermissionsMixin

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    pass

class UserManager(BaseUserManager):
    pass