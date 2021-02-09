from django.test import TestCase

from media_server.models import Genre


class GenreModelTests(TestCase):
    def test_create_unique_slug(self):
        genre1 = Genre.objects.create(name='genre 1')
        self.assertEqual(genre1.slug, 'genre-1')

        genre2 = Genre.objects.create(name='genre 1')
        self.assertNotEqual(genre2.slug, 'genre-1')
