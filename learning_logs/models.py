from django.db import models


class Topic(models.Model):
	"""User's theme"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Returns model string description."""
		return self.text
# Create your models here.
