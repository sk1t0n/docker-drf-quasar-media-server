from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.pagination import PageNumberPagination

from .models import Video, Genre
from .serializers import VideoSerializer, GenreSerializer


class VideoPagination(PageNumberPagination):
    page_size = 5


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


class GenrePagination(PageNumberPagination):
    page_size = 5


class GenreListCreateView(ListCreateAPIView):
    pagination_class = GenrePagination
    serializer_class = GenreSerializer

    def get_queryset(self):
        return Genre.objects.all()


class GenreRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Genre.objects.filter(slug=self.kwargs['slug'])
