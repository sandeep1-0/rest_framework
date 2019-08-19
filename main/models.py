from django.db import models


class BranchDetails(models.Model):
	branch_id = models.IntegerField(unique=True,primary_key=True)
	branch_name = models.CharField(max_length=100)


class StudentDetails(models.Model):
	student_id = models.IntegerField(unique=True,primary_key=True)
	student_name = models.CharField(max_length=50)
	branch_id = models.ForeignKey(BranchDetails, on_delete=models.CASCADE)


class MarkDetails(models.Model):
	student_id = models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
	Subject1 = models.IntegerField(default=0)
	Subject2 = models.IntegerField(default=0)
	Subject3 = models.IntegerField(default=0)