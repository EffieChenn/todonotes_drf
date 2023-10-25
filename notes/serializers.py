from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Note
        fields = "__all__"
