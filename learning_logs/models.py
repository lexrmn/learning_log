from django.db import models


# Create your models here.
class Topic(models.Model):
	"""User's theme"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Returns model string description."""
		return self.text


class Entry(models.Model):
	"""Information, learned by user about theme that interests him"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)


	class Meta:
		verbose_name_plural = 'enties'

	def __str__(self):
		"""Returns string model name."""
		return f"{self.text[:50]}..."

