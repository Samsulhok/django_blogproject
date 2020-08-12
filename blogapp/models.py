from django.db import models

class Blog(models.Model):
	title= models.CharField(max_length=200)
	image= models.ImageField(upload_to="blogs")
	content= models.TextField()
	date= models.DateTimeField(auto_now_add=True)
	auther= models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.title