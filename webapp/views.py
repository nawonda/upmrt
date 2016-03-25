from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Post

def index(request):
	return render(request, 'webapp/index.html')

def driver(request):	
	return render(request, 'webapp/driver.html')	

def help(request):	
	return render(request, 'webapp/help.html')	

def signup(request):	
	return render(request, 'webapp/signup.html')	

def login(request):	
	return render(request, 'webapp/login.html')	

def about(request):	
	return render(request, 'webapp/about.html')	

def contact(request):
	postObjects = Post.objects.all().order_by("-date")[:25]	
	return render(request, 'webapp/contact.html',{'info':postObjects})	
	# return render(request, 'webapp/contact.html',{'info':['jerry','jy1215jy@gmail.com']})	