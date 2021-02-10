from django.test import TestCase

from media_server.models import Genre


class GenreModelTests(TestCase):
    def setUp(self):
        self.genre1 = Genre.objects.create(name='genre 1')
        self.genre2 = Genre.objects.create(name='genre 2')

    def test_create_with_new_slug(self):
        new_genre = Genre.objects.create(name='new genre')
        self.assertEqual(new_genre.slug, 'new-genre')

    def test_create_with_existing_slug(self):
        new_genre = Genre.objects.create(name=self.genre1.slug)
        self.assertNotEqual(new_genre.slug, self.genre1.slug)

    def test_update_with_current_slug(self):
        self.genre1.slug = 'genre-1'
        self.genre1.save()
        self.assertEqual(self.genre1.slug, 'genre-1')

    def test_update_with_new_slug(self):
        self.genre1.slug = 'new-slug'
        self.genre1.save()
        self.assertEqual(self.genre1.slug, 'new-slug')

    def test_update_with_existing_slug(self):
        self.genre1.slug = self.genre2.slug
        self.genre1.save()
        self.assertNotEqual(self.genre1.slug, self.genre2.slug)
