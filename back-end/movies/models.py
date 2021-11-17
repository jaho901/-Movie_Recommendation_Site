from django.db import models
# from django.db import settings

# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    vote = models.FloatField()
    country = models.CharField(max_length=50)
    time = models.CharField(max_length=10)
    grade = models.CharField(max_length=10)
    poster_path = models.TextField()
    genre_1 = models.CharField(max_length=10)
    genre_2 = models.CharField(max_length=10, default='')
    genre_3 = models.CharField(max_length=10, default='')
    genre_4 = models.CharField(max_length=10, default='')
    actor_1 = models.CharField(max_length=20)
    actor_2 = models.CharField(max_length=20, default='')
    actor_3 = models.CharField(max_length=20, default='')
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField(default='')
    content = models.TextField()
    def __str__(self):
        return self.title
