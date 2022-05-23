from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    numPages = models.IntegerField()

    def __str__(self):
        return f'{self.title}'
