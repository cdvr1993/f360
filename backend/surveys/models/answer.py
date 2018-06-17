from django.db import models

from surveys.models.participant import Participant
from surveys.models.peer import Peer
from surveys.models.question import Question


class Answer(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    peer = models.ForeignKey(Peer, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.TextField()
