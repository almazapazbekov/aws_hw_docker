from django.contrib import admin

from .models import Category, QuestionAnswer

admin.site.register(Category)
admin.site.register(QuestionAnswer)