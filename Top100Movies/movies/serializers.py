from rest_framework import serializers

from .models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ("id", "title", "image", "rate","description", "is_watched", "place_in_top")

class MoviesSerializer2(serializers.ModelSerializer):
    def update(self,instance, validated_data):
        instance.is_watched = validated_data.get('is_watched', instance.is_watched)
        print(instance.is_watched)
        if instance.is_watched:
            instance.rate = validated_data.get('rate', instance.rate)
            instance.place_in_top = validated_data.get('place_in_top', instance.place_in_top)
        instance.save()
        return instance

    class Meta:
        model = Movies
        fields = ("id", "title", "rate","description", "is_watched", "place_in_top")
