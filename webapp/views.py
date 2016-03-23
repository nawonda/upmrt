from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Post


def index(request):
	return render(request, 'webapp/home.html')

def contact(request):

	postObjects = Post.objects.all().order_by("-date")[:25]	
	return render(request, 'webapp/contact.html',{'info':postObjects})	
	# return render(request, 'webapp/contact.html',{'info':['jerry','jy1215jy@gmail.com']})	