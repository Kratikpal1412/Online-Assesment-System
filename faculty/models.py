from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post5(models.Model):
	total_score=models.CharField(max_length=100)
	exam_name=models.TextField()
	subject_name=models.TextField()
	start_date=models.CharField(max_length=100)
	end_date=models.CharField(max_length=100)
	questions=models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)



	def __str__(self):
		return self.exam_name

	def get_absolute_url(self):
		return reverse('addexam')

class Notification(models.Model):
	message=models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
