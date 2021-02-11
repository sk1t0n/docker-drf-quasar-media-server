from hashlib import shake_256
from time import time

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify


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
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        ordering = ('-release_date', 'title')

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.fields.CharField('name', max_length=100)
    slug = models.fields.SlugField(
        'slug', max_length=110, blank=True, unique=True, allow_unicode=True
    )

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'
        ordering = ('name',)

    def __str__(self):
        return self.name


def set_unique_slug(sender, instance, *args, **kwargs):
    # update slug:
    if instance.id:
        db_obj = sender.objects.filter(pk=instance.id).first()
        # old and new slugs are equal
        if db_obj.slug == instance.slug:
            return

    # create slug
    if not instance.slug:
        if isinstance(instance, Video):
            slug = slugify(instance.title)
        else:
            slug = slugify(instance.name)
    # # update slug
    else:
        slug = instance.slug

    qs = sender.objects.filter(slug=slug).first()
    if qs:
        hash = shake_256(str(time()).encode()).hexdigest(5)
        slug = f'{slug}-{hash}'
    instance.slug = slug


pre_save.connect(set_unique_slug, sender=Video)
pre_save.connect(set_unique_slug, sender=Genre)
