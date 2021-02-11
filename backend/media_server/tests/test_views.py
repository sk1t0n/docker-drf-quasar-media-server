import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from media_server.models import Video, Genre
from media_server.serializers import VideoSerializer


class VideoListCreateViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        video1_data = {
            'title': 'Video 1',
            'description': 'Description 1',
            'release_date': '2020-10-20',
            'runtime': 65,
            'url': 'url1'
        }
        self.video1 = Video.objects.create(**video1_data)

        self.genre1 = Genre.objects.create(name='genre 1')
        self.genre2 = Genre.objects.create(name='genre 2')

        self.video1.genres.add(self.genre1)
        self.video1.genres.add(self.genre2)

        self.data = {
            'title': 'New Video',
            'description': 'Description of the new video',
            'release_date': '2014-02-15',
            'runtime': 92,
            'url': 'url2'
        }

    def test_read_video_list(self):
        response = self.client.get(reverse('video_list_create'))
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)

        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_video_with_empty_genre_list(self):
        self.data['genres'] = []
        response = self.client.post(
            reverse('video_list_create'),
            data=json.dumps(self.data),
            content_type='application/json'
        )

        added_video = Video.objects.filter(title=self.data['title']).first()
        serializer = VideoSerializer(instance=added_video)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_video_with_filled_genre_list(self):
        self.data['genres'] = [
            {'name': 'genre 1'},
            {'name': 'new genre'}
        ]
        response = self.client.post(
            reverse('video_list_create'),
            data=json.dumps(self.data),
            content_type='application/json'
        )

        added_video = Video.objects.filter(title=self.data['title']).first()
        serializer = VideoSerializer(instance=added_video)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class VideoRetrieveUpdateDestroyViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        video1_data = {
            'title': 'Video 1',
            'description': 'Description 1',
            'release_date': '2020-10-20',
            'runtime': 65,
            'url': 'url1'
        }
        self.video1 = Video.objects.create(**video1_data)

        self.genre1 = Genre.objects.create(name='genre 1')
        self.genre2 = Genre.objects.create(name='genre 2')

        self.video1.genres.add(self.genre1)
        self.video1.genres.add(self.genre2)

    def test_read_video(self, *args, **kwargs):
        response = self.client.get(
            reverse('video_read_update_delete', kwargs={'slug': self.video1.slug})
        )
        serializer = VideoSerializer(instance=self.video1)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_video(self, *args, **kwargs):
        data = {
            'title': 'New Title',
            'description': 'New Description',
            'release_date': '2005-05-25',
            'runtime': 45,
            'url': 'url',
            'genres': [
                {'name': 'new genre1'},
                {'name': 'new genre2'}
            ]
        }
        response = self.client.put(
            reverse('video_read_update_delete', kwargs={'slug': self.video1.slug}),
            data=json.dumps(data),
            content_type='application/json'
        )

        updated_video = Video.objects.filter(title=data['title']).first()
        serializer = VideoSerializer(instance=updated_video)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_video(self, *args, **kwargs):
        response = self.client.delete(
            reverse('video_read_update_delete', kwargs={'slug': self.video1.slug}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
