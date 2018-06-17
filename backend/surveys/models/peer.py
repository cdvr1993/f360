from django.db import models

from surveys.models.person import Person
from surveys.models.participant import Participant


class Peer(Person):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
