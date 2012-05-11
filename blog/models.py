from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=75)
	post = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	mod_date = models.DateTimeField(auto_now=True)
	pub_date = models.DateTimeField()

	def __unicode__(self):
		return self.title
