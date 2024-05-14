from django.db import models
from datetime import date
from django.utils import timezone

class Project(models.Model):
    technologies = models.ManyToManyField('Technology')
    repo_link = models.CharField(max_length=200,null = True, blank = True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length = 500, null = True, blank = True)
    date = models.DateField(default = timezone.now)
    def __str__(self) -> str:
        return self.title



class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self) -> str:
        return self.name
