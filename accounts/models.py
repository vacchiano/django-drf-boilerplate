from django.db import models

from authemail.models import EmailAbstractUser, EmailUserManager

class MyUser(EmailAbstractUser):
	# Custom fields
	# date_of_birth = models.DateField('Date of birth', null=True, blank=True)

	# Required
	objects = EmailUserManager()