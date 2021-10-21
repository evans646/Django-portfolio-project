from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=300,default="project description")
 #function to return the summary so inside the db we will get a summary of the project instead of just object1 and so on 
    def __str__(self):
        return self.summary
