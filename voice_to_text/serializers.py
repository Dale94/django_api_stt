# myapp/serializers.py

from rest_framework import serializers
from .models import AudioFile

class AudioFileSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   comments = serializers.FileField()
