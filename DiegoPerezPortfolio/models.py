from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ## need a way for a list of images maybe
    def __str__(self):
        return self.title


class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()
    caption = models.TextField(blank = True)
    def __str__(self):
        return f"Image for {self.project.title}"