from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a new field for testing out our API view"""
    name = serializers.CharField(max_length=10)
