from django.http import Http404
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
)
from rest_framework.pagination import PageNumberPagination

from .models import Video, Genre
from .serializers import VideoSerializer, GenreSerializer

VIDEOS_PER_PAGE = 6


class VideoPagination(PageNumberPagination):
    page_size = VIDEOS_PER_PAGE


class VideoListCreateView(ListCreateAPIView):
    pagination_class = VideoPagination
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.all()


class VideoRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = VideoSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Video.objects.filter(slug=self.kwargs['slug'])

    def update(self, request, *args, **kwargs):
        if 'genres' in request.data:
            request.data['genres_old'] = request.data.pop('genres')
        request.data['genres'] = []
        return super(VideoRetrieveUpdateDestroyView, self) \
            .update(request, *args, **kwargs)


class GenreListCreateView(ListCreateAPIView):
    serializer_class = GenreSerializer

    def get_queryset(self):
        return Genre.objects.all()


class GenreRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Genre.objects.filter(slug=self.kwargs['slug'])


class GenreListVideo(ListAPIView):
    pagination_class = VideoPagination
    serializer_class = VideoSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        genre = Genre.objects.filter(slug=slug).first()
        if genre:
            return genre.videos.all()
        else:
            raise Http404
