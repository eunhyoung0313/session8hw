from django.db import models
        
class Post(models.Model):
    GENRE_CHOICES={
        ('movie', 'Movie'),
        ('drama', 'Drama'),
        ('entertainment','Entertainment')
    }
    genre=models.CharField(max_length=200, choices=GENRE_CHOICES, null=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    time=models.TextField()
    

    def __str__(self):
        return self.title
# Create your models here.
