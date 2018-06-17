from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=80)
