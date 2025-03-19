from rest_framework import serializers

class ChatMessageSerializer(serializers.Serializer):
    sender = serializers.CharField()
    message = serializers.CharField()
    timestamp = serializers.DateTimeField()
