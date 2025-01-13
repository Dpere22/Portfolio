import os

from django.db import models

from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(blank=True, null=True)
    ## need a way for a list of images maybe
    def __str__(self):
        return self.title

@receiver(post_delete, sender=Project)
def delete_image_on_project_delete(sender, instance, **kwargs):
    if instance.thumbnail:
        if os.path.isfile(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()
    caption = models.TextField(blank = True)
    def __str__(self):
        return f"Image for {self.project.title}"
    ##note, if in admin add pictures with path /media/filename

@receiver(post_delete, sender=ProjectImages)
def delete_images_on_project_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)