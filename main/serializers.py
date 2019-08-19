from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *


class BranchSerializer(serializers.ModelSerializer):
	class Meta:
		model = BranchDetails
		fields = ['branch_id','branch_name']


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentDetails
		fields = ['student_id','student_name','branch_id']


class MarkSerializer(serializers.ModelSerializer):
	# student = StudentSerializer(source=StudentDetails, read_only=True)
	# branch = BranchSerializer(source=BranchDetails, read_only=True)

	student_name = serializers.CharField(source='student_id.student_name')
	branch_name = serializers.CharField(source='student_id.branch_id.branch_name')
	
	class Meta:
		model = MarkDetails
		fields = '__all__'