from rest_framework import serializers
from .models import *

class NoticeContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = (
            "id",
            "title",
            "content",
            "written_date",
        )

class NoticeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = (
            "id",
            "title",
            "written_date",
        )
        
class QnaContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "title",
            "content",
            "writer",
            "writer_email",
            "solvebool",
            "written_date",
            "recent_updated",
        )

class QnaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "title",
            "writer",
            "written_date",
            "solvebool",
        )

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            "post",
            "author",
            "message",
            "created",
            "updated",
        )