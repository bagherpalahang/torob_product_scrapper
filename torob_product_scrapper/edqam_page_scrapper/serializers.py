from rest_framework import serializers
from .models import EdghamPage

class EdghamPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EdghamPage
        exclude = ('id', )