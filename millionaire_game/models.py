from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Question(models.Model):
    text = models.TextField()
    complexity = models.SmallIntegerField(validators=[MaxValueValidator(20), MinValueValidator(5)])


class Answer(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)


class GameSession(models.Model):
    session = models.UUIDField()
    answers = models.ManyToManyField(Answer)
