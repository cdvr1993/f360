from django.db import models


class Person(models.Model):
    class Meta:
        abstract = True

    answered = models.BooleanField(default=False)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=256)
    job = models.CharField(max_length=80)
