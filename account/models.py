from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, first_name, last_name, password=None):
		if not email:
			raise ValueError("Users must have an email")
		if not username:
			raise ValueError("Users must have an username")
		if not first_name:
			raise ValueError("Users must have a first name")
		if not last_name:
			raise ValueError("Users must have a last name")

		user = self.model(
				email = self.normalize_email(email),
				username = username,
				first_name = first_name.title(),
				last_name = last_name.title()

			)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, first_name, last_name, password):
		user = self.create_user(
				email = self.normalize_email(email),
				username = username,
				first_name = first_name.title(),
				last_name = last_name.title(),
				password = password

			)

		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
	username = models.CharField(max_length=30, unique=True)
	date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
	last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	# USERNAME_FIELD is what you want the user to login with
	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["username", "first_name", "last_name"]

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

