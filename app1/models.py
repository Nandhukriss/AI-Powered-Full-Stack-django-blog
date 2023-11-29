from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (
("Tech", "Tech"),
("Entertainment", "Entertainment"),
("Educational", "Educational"),
)

class Post(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.TextField()
    blog_content=models.TextField(default="")
    date_added=models.DateField(auto_now_add=True,null=True,blank=True)
    post_image=models.ImageField(upload_to='Posts',default='uploads/Posts/default.png')
    Category= models.CharField(max_length=255,choices=CATEGORY_CHOICES,default="Entertainment")

    def __str__(self) :
        return self.title
