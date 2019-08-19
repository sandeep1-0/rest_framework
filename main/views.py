import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import JsonResponse



class StudentView(APIView):
	"""
	List all users, or create a new user.
	"""
	def get(self, request, format=None):
		student_info = MarkDetails.objects.all()
		serializer = MarkSerializer(student_info, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		data = request.data
		print(data)
		branch = BranchDetails.objects.create(branch_id=data.get('branch_id'),branch_name=data.get('branch_name'))
		student = StudentDetails.objects.create(student_id=data.get('student_id'),student_name=data.get('student_name'),branch_id=branch)
		marks=MarkDetails.objects.create(Subject1=data.get('subject1'),Subject2=data.get('subject2'),Subject3=data.get('subject3'),student_id=student)

		return Response({'msg': 'data created succesfully'}, status=status.HTTP_201_CREATED)
