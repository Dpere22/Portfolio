from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(blank=True, null=True)
    ## need a way for a list of images maybe
    def __str__(self):
        return self.title