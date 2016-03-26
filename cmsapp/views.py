from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'cmsapp/index.html')

def blank(request):
	return render(request, 'cmsapp/blank.html')

def buttons(request):	
	return render(request, 'cmsapp/buttons.html')	

def flot(request):	
	return render(request, 'cmsapp/flot.html')	

def forms(request):	
	return render(request, 'cmsapp/forms.html')	

def grid(request):	
	return render(request, 'cmsapp/grid.html')	

def icons(request):	
	return render(request, 'cmsapp/icons.html')	

	