from django.db import models

# Create your models here.
class Users(models.Model):
	"""Users of our blog post"""
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=20)
	email = models.EmailField()
	
	
