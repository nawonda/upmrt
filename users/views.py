from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

def show(request):
	
	user_profile = Profile.objects.filter(user=1)

	return render(request, 'users/show.html',{'profile':user_profile})

def edit(request):
	return render(request, 'users/edit.html')