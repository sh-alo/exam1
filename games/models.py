from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100, null=False)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Create your models here.
