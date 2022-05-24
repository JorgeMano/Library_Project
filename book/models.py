from django.db import models
#from author.models import Author

class Book(models.Model):
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    numPages = models.IntegerField()
    #author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}'
