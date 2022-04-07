from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

	image = models.ImageField()
	description = models.CharField(max_length=200, blank=True, null=True)
	date_added = models.DateTimeField(auto_now=True)
	likes = models.ManyToManyField(User, related_name='likes')
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.description

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)
	content = models.CharField(max_length=300)
	date_added = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username + ' | ' + str(self.content)


class Profile(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	avatar = models.ImageField(null=True, blank=True)
	bio = models.TextField(max_length=300, blank=True, null=True)
	connection_url = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.user.username
