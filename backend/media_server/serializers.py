from rest_framework import serializers

from .models import Video, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=False)

    class Meta:
        model = Video
        fields = '__all__'

    def create(self, validated_data):
        """Handle writable nested serializer to create a new video.

        Args:
            validated_data (dict): validated data, by serializer class's validate method
        Returns:
            Video: updated Video model instance
        """
        try:
            genres_data = validated_data.pop('genres')
            video = Video.objects.create(**validated_data)

            for genre_data in genres_data:
                genre, _ = Genre.objects.get_or_create(**genre_data)
                video.genres.add(genre)

            return video
        except TypeError:
            video.delete()
            raise TypeError('Got a TypeError while creating the video')

    def update(self, instance, validated_data):
        """
        Handle writable nested serializer to update the current video.
        Genres are replaced but not added.

        Args:
            instance (Video): current Video model instance
            validated_data (dict): validated data, by serializer class's validate method
        Returns:
            Video: updated Video model instance
        """
        validated_data.pop('genres')
        instance = super(VideoSerializer, self).update(instance, validated_data)

        genres_data = self.context['request'].data['genres_old']
        genres = []
        for genre_data in genres_data:
            qs = Genre.objects.filter(name=genre_data['name'])
            if qs.exists():
                genre = qs.first()
            else:
                genre = Genre.objects.create(**genre_data)
            genres.append(genre)
            # replace genres
            instance.genres.set(genres)
        instance.save()

        return instance
