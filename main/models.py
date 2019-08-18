from django.db import models

class Actor(models.Model):
	login = models.CharField(max_length=100)
	avatar_url = models.CharField(max_length=100)

class Repo(models.Model):
	name = models.CharField(max_length=100)
	url = models.CharField(max_length=100)	

class Event(models.Model):
	event_type = models.CharField(max_length=100)
	actor = models.ForeignKey(Actor, related_name='actors', on_delete=models.CASCADE)
	repo = models.ForeignKey(Repo, related_name='repos', on_delete=models.CASCADE)
