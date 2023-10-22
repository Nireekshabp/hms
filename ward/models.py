from django.db import models

# Create your models here.


class Ward(models.Model):

	name = models.CharField(max_length=40)
	number = models.CharField(max_length=4)

	def __str__(self):
		return f"{self.name} - {self.number}"

