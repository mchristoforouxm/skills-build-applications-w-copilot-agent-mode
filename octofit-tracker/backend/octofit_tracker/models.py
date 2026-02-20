from django.db import models
from djongo import models as djongo_models
from bson import ObjectId

class User(models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

class Team(models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

class Activity(models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = djongo_models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()  # in minutes
    date = models.DateField()

class Leaderboard(models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    team = djongo_models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)

class Workout(models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=50)
