from django.test import TestCase
from django.urls import reverse, resolve

from media_server.views import (
    VideoListCreateView,
    VideoRetrieveUpdateDestroyView,
    GenreListCreateView,
    GenreRetrieveUpdateDestroyView
)


class VideoListCreateViewUrlsTests(TestCase):
    def test_urls(self):
        url = reverse('video_list_create')
        self.assertEqual(resolve(url).func.view_class, VideoListCreateView)


class VideoRetrieveUpdateDestroyViewUrlsTests(TestCase):
    def test_urls(self):
        url = reverse('video_read_update_delete', kwargs={'slug': 'video-1'})
        self.assertEqual(resolve(url).func.view_class, VideoRetrieveUpdateDestroyView)


class GenreListCreateViewUrlsTests(TestCase):
    def test_urls(self):
        url = reverse('genre_list_create')
        self.assertEqual(resolve(url).func.view_class, GenreListCreateView)


class GenreRetrieveUpdateDestroyViewUrlsTests(TestCase):
    def test_urls(self):
        url = reverse('genre_read_update_delete', kwargs={'slug': 'genre-1'})
        self.assertEqual(resolve(url).func.view_class, GenreRetrieveUpdateDestroyView)
