from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    dat = models.DateField()
    desc = models.TextField()

