from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    # def create_user(self, email, cnic, username=None, password=None):
    def create_user(self, email, CNIC, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not CNIC:
            raise ValueError("Users must have a CNIC number")

        user = self.model(
            email = self.normalize_email(email),
            # username = username,
            CNIC = CNIC,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    # def create_superuser(self, email, cnic, password, username=None):
    def create_superuser(self, email, CNIC, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            # username = username,
            CNIC = CNIC,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class Account(AbstractBaseUser):
    email                   = models.EmailField(verbose_name="email", max_length=60, unique=True)
    # username                = models.CharField(max_length=30, unique=True, null=True, blank=True)
    CNIC                    = models.CharField(max_length=15, unique=True, verbose_name="CNIC number")
    date_joined             = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['CNIC']

    objects = MyAccountManager()

    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
  
