from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
	"""docstring for BlogPost"""
	title = models.CharField(max_length=100)
	content = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now
		self.save()


		

		