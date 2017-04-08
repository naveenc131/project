from django.db import models
from django.utils import timezone

# Create your models here.
class Users(models.Model):
	"""docstring for Users"""
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	
	email = models.EmailField()
	password = models.CharField(max_length=30)

	about_me = models.CharField(max_length=100)


class BlogPost(models.Model):
	"""docstring for BlogPost"""
	title = models.CharField(max_length=100)
	content = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now
		self.save()


		

		