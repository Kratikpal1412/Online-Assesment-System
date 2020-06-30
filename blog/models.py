from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	obtain_score=models.CharField(max_length=100)
	total_score=models.CharField(max_length=100)
	quiz_name=models.TextField()
	status=models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)

class Post3(models.Model):
	obtain_score=models.CharField(max_length=100)
	total_score=models.CharField(max_length=100)
	quiz_name=models.TextField()
	status=models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)



	def __str__(self):
		return self.quiz_name
