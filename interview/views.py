from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from .models import Category, QuestionAnswer
from .serializers import CategorySerializer, QuestionAnswerSerializerWithAnswer, QuestionAnswerSerializerNoAnswer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerListCreateAPIView(generics.ListCreateAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializerNoAnswer
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    ordering = ['-importance', ]
    search_fields = ['question', ]
    filterset_fields = ['category', ]


class QuestionAnswerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializerWithAnswer
