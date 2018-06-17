from django.db import models

from surveys.models.generation import Generation
from surveys.models.person import Person
from surveys.models.survey import Survey


class Participant(Person):
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
