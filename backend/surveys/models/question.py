from django.db import models

from surveys.models.category import Category
from surveys.models.survey import Survey


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    statement = models.CharField(max_length=256)
    choices = models.TextField(null=True)
