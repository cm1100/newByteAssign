from rest_framework import serializers
from url.models import UrlDetail


class UrlDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrlDetail
        fields = '__all__'