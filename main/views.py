import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from main.models import Actor, Repo, Event
from main.serializers import ActorSerializer, RepoSerializer, EventSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


class ActorViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Actor.objects.all()
	serializer_class = ActorSerializer

class RepoViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Repo.objects.all()
	serializer_class = RepoSerializer

class EventViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Event.objects.all()
	serializer_class = EventSerializer

class EventView(APIView):
	"""
	List all users, or create a new user.
	"""
	def get(self, request, format=None):
		events = Event.objects.all()
		serializer = EventSerializer(events, many=True)
		return Response(serializer.data)
	
	def post(self, request, format=None):
		data = request.data
		actor = Actor(login=data['actor']['login'], avatar_url=data['actor']['avatar_url'])
		actor.save()
		repo = Repo(name=data['repo']['name'], url=data['repo']['url'])
		repo.save()
		event = Event(event_type=data['event_type'], actor=actor, repo=repo)
		event.save()
		return Response({'msg': 'data created succesfully'}, status=status.HTTP_201_CREATED)

	def delete(self, request, format=None):
		data = request.data
		event = Event.objects.get(id=data['event_id'])
		event.delete()
		return Response({'msg': 'data deleted succesfully'}, status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def auth_login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return JsonResponse({'msg': 'User loged in succesfully'}, safe=False)
	else:
		return JsonResponse({'msg': 'Username or password is wrong'}, safe=False)
