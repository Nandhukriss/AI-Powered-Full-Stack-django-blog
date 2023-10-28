from django.db import models

# Create your models here.


class Post(models.Model):
    
    name=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    content=models.TextField()
    date_added=models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self) :
        return self.title
