from django.db import models

class Login(models.Model):
	loginId = models.CharField(max_length=10)
	userName = models.CharField(max_length=25)
	password = models.CharField(max_length=25)

class User(models.Model):
	userId = models.CharField(max_length=25)
	loginId = models.ForeignKey(Login, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	areaOfInterest=models.CharField(max_length=50)
	role = models.CharField(max_length=20)
	emailId = models.EmailField(max_length=50)
	resumeDoc = models.FileField(upload_to='NYUTeamUp/teamupapp/storage/',default='NYUTeamUp/teamupapp/storage/')

class Project(models.Model):
	projectId = models.CharField(max_length=25)
	projectName = models.CharField(max_length=50)
	userId = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.CharField(max_length=25)
	description = models.TextField()

class Job(models.Model):
	jobId = models.CharField(max_length=25)
	projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
	requirement = models.TextField()
	timeStamp = models.DateTimeField()
	numOfPositions = models.IntegerField()

class Application(models.Model):
	appId=models.CharField(max_length=25)
	jobId = models.ForeignKey(Job, on_delete=models.CASCADE)
	userId = models.ForeignKey(User, on_delete=models.CASCADE)
