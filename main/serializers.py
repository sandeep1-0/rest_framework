from django.contrib.auth.models import User, Group
from rest_framework import serializers

from main.models import Actor, Repo, Event

class ActorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Actor
		fields = ('id', 'login', 'avatar_url')

class RepoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Repo
		fields = ('id', 'name', 'url')

class EventSerializer(serializers.HyperlinkedModelSerializer):
	actors = ActorSerializer(source='actor', read_only=True)
	repos = RepoSerializer(source='repo', read_only=True)
	
	class Meta:
		model = Event
		fields = ('id', 'event_type', 'actors', 'repos')
