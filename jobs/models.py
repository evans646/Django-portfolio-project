from django.db import models
from cloudinary.models import CloudinaryField




# Create your models here.
class Job(models.Model):
    image = CloudinaryField('image')
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=2000,default="project description")
    url = models.CharField(max_length=200,default="project url")
 #function to return the summary so inside the db we will get a summary of the project instead of just: object1 and so on .....
    def __str__(self):
        return self.summary


