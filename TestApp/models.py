from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField()    

    def __str__(self):
        return f'{self.name} - {self.rating}%'

