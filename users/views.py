from django.shortcuts import render
from django.http import HttpResponse

def show(request):
	return render(request, 'users/show.html')

def edit(request):
	return render(request, 'users/edit.html')