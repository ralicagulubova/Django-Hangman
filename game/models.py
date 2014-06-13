from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode


class Profile(models.Model):
	user =  models.OneToOneField(User)
	play_game = models.BooleanField(default=False)
	create_game = models.BooleanField(default=False)
	finished_game = models.BooleanField(default=False)
	score = models.IntegerField(default=0)
	wined_game = models.BooleanField(default=False)
	lost_game = models.BooleanField(default=False)


class Game(models.Model):
	created_by = models.ForeignKey(Profile)
	word = models.CharField(max_length = 20)
	description = models.TextField(max_length = 20)
	right_guess = models.CharField(max_length = 40)
	wrong_guess = models.CharField(max_length = 40)
	player = models.IntegerField(default=0)