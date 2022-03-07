from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.text import slugify
import string, random
from django.shortcuts import render, redirect, reverse

# Create your models here.

USER_TYPE_USER = 'USER'                     # user
USER_TYPE_OWNER = 'OWNER'                   # store owner
USER_TYPE_SUPERUSER = 'SUPERUSER'           # admin

USER_TYPE_CHOICES = (
    (USER_TYPE_USER, USER_TYPE_USER),
    (USER_TYPE_OWNER, USER_TYPE_OWNER),
    (USER_TYPE_SUPERUSER, USER_TYPE_SUPERUSER),
)

class NewUser( BaseUserManager):
    def create_user(self, email, phone=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            phone = phone,
        )

        if password is not None:
            user.set_password( password)

        user.save( using=self._db)
        return user

    def create_superuser(self, email, phone, password):
        user = self.create_user(
            email,
            phone,
            password=password,
        )

        user.type = USER_TYPE_SUPERUSER
        user.save(using=self._db)

        return user

class NewCustomUser( AbstractBaseUser):

    email = models.EmailField(verbose_name='Email Address', max_length=255, unique=True)
    phone = models.CharField(max_length=200, null=False, blank=False)
    # is_active is checked in rest_framework_simplejwt.authentication.JWTAuthentication
    # if is_active is False, JWT Authentication failed
    is_active = models.BooleanField(verbose_name='User Active?', default=True)
    type = models.CharField(verbose_name='User Type', max_length=20, choices=USER_TYPE_CHOICES, default=USER_TYPE_USER)
    created = models.DateTimeField("Created", auto_now_add=True)
    slug = models.SlugField(db_index=True, unique=True, allow_unicode=True)

    objects = NewUser()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural ='Users'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        return True if self.is_active and self.type == USER_TYPE_SUPERUSER else False

    def has_module_perms(self, app_label):
        # Returns True if the user has permission to access models in the given app.
        return True if self.is_active and self.type == USER_TYPE_SUPERUSER else False

    @property
    def is_staff(self):
        # Returns True if the user is allowed to have access to the admin site.
        return True if self.is_active and self.type == USER_TYPE_SUPERUSER else False

    def save(self, *args, **kwargs):
        slug_suffix = []
        for i in range(10):
            slug_suffix.append( random.choice(string.ascii_letters))
        self.slug = slugify(self.email.split("@")[0]+''.join(slug_suffix), allow_unicode=True)
        super().save(*args, **kwargs)

