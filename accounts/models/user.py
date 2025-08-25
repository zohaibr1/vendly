from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# -----------------------
# Custom User Manager
# -----------------------
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The Username must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("role", "customer")   # 👈 default customers
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")      # 👈 force admins

        return self._create_user(username, email, password, **extra_fields)


# -----------------------
# Custom User Model
# -----------------------
class User(AbstractUser):
    ROLE_CHOICES = (
        ("customer", "Customer"),
        ("vendor", "Vendor"),
        ("admin", "Admin"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="customer")
    vendor_approved = models.BooleanField(default=False)
    # Attach manager
    objects = UserManager()

    def __str__(self):
        return self.username
