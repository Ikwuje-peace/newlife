from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=250, null=True)
    subtitle = models.CharField(max_length=250, null= True)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
