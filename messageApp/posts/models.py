from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50] # this will display the first 50 characters of the text field
    

    