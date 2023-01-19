from rest_framework import serializers

from .models import Category, QuestionAnswer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class QuestionAnswerSerializerNoAnswer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = "__all__"
        read_only_fields = ['answer', ]


class QuestionAnswerSerializerWithAnswer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = "__all__"
