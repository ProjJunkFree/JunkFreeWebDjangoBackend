from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, 
    AbstractBaseUser, 
    PermissionsMixin
)
from django.conf import settings
 


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """ **kwargs meaning kay keyword arguments
        same ra ang 
        def create_user(self, first_name, last_name, email, password=None):
        sa naay kwargs
        """
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        # Gabuhaton sa normalized is e lowecase ang after sa @
        # Ex. jieclarkm@GMAIL.COM => jieclarkm@gmail.com
        email = email.lower()
        # So e lowercase niya tanan from first to end of characters

        user = self.model(
            email=email,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
    
        user = self.create_user(
            email,
            password=password,
            **kwargs
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        unique=True,
        max_length=255,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
