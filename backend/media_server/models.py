from django.db import models
from django.core.validators import MinValueValidator


class Video(models.Model):
    title = models.fields.CharField('title', max_length=100)
    slug = models.fields.SlugField(
        'slug', max_length=110, blank=True, unique=True, allow_unicode=True
    )
    description = models.fields.TextField('description', max_length=800)
    release_date = models.fields.DateField(
        'release_date', auto_now=False, auto_now_add=False
    )
    runtime = models.fields.IntegerField(
        'runtime', validators=[MinValueValidator(1)]
    )
    url = models.fields.CharField('url', max_length=200)
    genres = models.ManyToManyField('Genre', related_name='videos')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.fields.CharField('name', max_length=100)
    slug = models.fields.SlugField(
        'slug', max_length=110, blank=True, unique=True, allow_unicode=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
