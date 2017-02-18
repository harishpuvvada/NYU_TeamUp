from django.shortcuts import render
from django.views import generic

from teamupapp.models import Login,User,Project,Job,Application


class LandingView(generic.ListView):
	template_name = 'teamupapp/index.html'
	context_object_name = 'category_list'
	#category_list = Project.objects.order_by('category').distinct('category')

	def get_queryset(self):
		project_list =  Project.objects.all()
		category_list = []
		for project in project_list:
			category_list.append(project.category)
		category_list = set(category_list)
		return category_list

class ProjListView(generic.ListView):
	template_name = 'teamupapp/list.html'
	context_object_name = 'project_list'

class ProjDetailView(generic.DetailView):
	template_name = ''

class MyProjsView(generic.ListView):
	template_name = ''

class MyAppsView(generic.ListView):
	template_name = ''
