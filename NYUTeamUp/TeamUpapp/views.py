from django.shortcuts import render

from TeamUpapp.models import Login,User,Project,Job,Application


def index(request):
	items = Item.objects.exclude(amount=0)
	return render(request,'TeamUpapp/login.html',{

		'items':items,

	})

def item_detail(request,id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request,'firstapp/item_detail.html',{'item':item,})