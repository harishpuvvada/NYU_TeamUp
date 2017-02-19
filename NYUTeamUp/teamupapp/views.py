from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from teamupapp.models import Login,User,Project,Job,Application

class LandingView(generic.ListView):
	template_name = 'teamupapp/index.html'
	context_object_name = 'project_list'

	def get_queryset(self):
		project_list =  Project.objects.all()
		return project_list

class MyProjsView(generic.ListView):
	template_name = ''

class MyAppsView(generic.ListView):
	template_name = ''

def myApplications(request, userId):
	myAppsList = Application.objects.filter(userId=userId)
	return render(request, 'teamupapp/myapps.html', {'myAppslist': myAppsList})

def myProjList(request, userId):
	myProjList = Project.objects.filter(userId=userId)
	return render(request, 'teamupapp/myproj.html', {'mylist':myProjList})

def projDetail(request, projectId):
	project = Project.objects.filter(projectId=projectId)
	job_list = Job.objects.filter(projectId=projectId)
	return render(request, 'teamupapp/detail.html', {'job_list':job_list})

def projList(request, category):
	project_list = Project.objects.filter(category=category)
	return render(request, 'teamupapp/list.html', {'project_list':project_list})