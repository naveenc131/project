from django import forms
from django.forms import ModelForm
from django.db import models

class UserLoginForm(models.Model):
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=20)

	class Meta:
		model = Users
		fields = ['username', 'password']

	def validate_login_data():
		
					


