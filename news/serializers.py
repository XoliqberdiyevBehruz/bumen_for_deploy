from rest_framework import serializers

from news.models import News
from common.serializers import MediaURlSerializer


class NewsListSerializer(serializers.ModelSerializer):
    image = MediaURlSerializer(read_only=True)

    class Meta:
        model = News
        fields = ("id", "title", "description", "created_at", "image")
