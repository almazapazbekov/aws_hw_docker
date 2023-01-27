from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate(value):
    if value <= 0 or value > 100:
        raise ValidationError(
            _('%(value)больше 100 или меньше 0'),
            params={'value': value},
        )


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class QuestionAnswer(models.Model):
    question = models.CharField(max_length=255)
    short_answer = models.CharField(max_length=255)
    answer = models.TextField(null=True, blank=True)
    importance = models.IntegerField(validators=[validate])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
