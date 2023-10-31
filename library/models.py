from django.db import models

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=64)
    abstract = models.TextField(blank=True, default="")

    def __str__(self):
        return self.title