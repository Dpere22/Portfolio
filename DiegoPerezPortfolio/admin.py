from django.contrib import admin

# Register your models here.
from .models import Project, ProjectImages


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ProjectImages)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ()