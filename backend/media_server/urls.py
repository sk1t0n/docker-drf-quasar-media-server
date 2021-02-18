from django.urls import path

from media_server import views

urlpatterns = [
    path('videos/', views.VideoListCreateView.as_view(), name='video_list_create'),
    path(
        'videos/<slug:slug>/',
        views.VideoRetrieveUpdateDestroyView.as_view(),
        name='video_read_update_delete'
    ),
    path(
        'genres/<slug:slug>/videos/',
        views.GenreListVideo.as_view(),
        name='genre_list_video'
    ),
    path('genres/', views.GenreListCreateView.as_view(), name='genre_list_create'),
    path(
        'genres/<slug:slug>/',
        views.GenreRetrieveUpdateDestroyView.as_view(),
        name='genre_read_update_delete'
    )
]
