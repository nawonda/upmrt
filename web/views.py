from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'web/index.html')

def login(request):
	return render(request, 'web/login.html')

def signup(request):
	return render(request, 'web/signup.html')

def contact(request):
	return render(request, 'web/contact.html')

def about(request):
	return render(request, 'web/about.html')