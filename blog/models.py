from django.db import models

# Create your models here.
class Users(models.Model):
	username = models.CharField(max_length=20)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)

	def __unicode__(self):
		return self.username

class Post(models.Model):
	title = models.CharField(max_length=75)
	post = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	mod_date = models.DateTimeField(auto_now=True)
	pub_date = models.DateTimeField()
	author = models.ForeignKey(Users)

	def __unicode__(self):
		return self.title
