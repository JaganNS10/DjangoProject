from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.



  
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author  =  models.ForeignKey(User,on_delete = models.CASCADE)

	# date_posted = models.DateTimeField(auto_now=True) 
	# date_posted = models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.title
		#return f"Title:{self.title},Content:{self.content},DateTime:{self.date_posted},Author:{self.author}"
	def get_absolute_url(self):
		return reverse('post_detail',kwargs={'pk':self.pk})	
		
#To Create Objects
#post_1 = Post(title='Blog_1',content = 'First Blog Content!',author=user) user = User.objects.first()
