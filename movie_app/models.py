from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, verbose_name='Write description of the film')
    duration = models.DurationField(blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    descript = models.TextField(blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.descript
