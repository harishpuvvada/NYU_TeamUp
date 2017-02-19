from django.contrib import admin

from .models import Login,User,Project,Application,Job


class LoginAdmin(admin.ModelAdmin):
	list_display = ['loginId','userName', 'password']

admin.site.register(Login,LoginAdmin)

class UserAdmin(admin.ModelAdmin):
	list_display = ['userId','loginId', 'name', 'areaOfInterest', 'role', 'emailId','resumeDoc']

admin.site.register(User,UserAdmin)


class ProjectAdmin(admin.ModelAdmin):
	list_display = ['projectId','projectName', 'userId', 'category', 'description']

admin.site.register(Project,ProjectAdmin)


class JobAdmin(admin.ModelAdmin):
	list_display = ['jobId','projectId', 'jobName', 'requirement', 'timeStamp', 'numOfPositions']

admin.site.register(Job,JobAdmin)


class ApplicationAdmin(admin.ModelAdmin):
	list_display = ['appId','jobId', 'userId']

admin.site.register(Application,ApplicationAdmin)





