from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
	return render(request, 'cmsapp/dashboard.html')
	
@login_required
def profile(request):
	return render(request, 'cmsapp/profile.html')

@login_required
def routes(request):	
	return render(request, 'cmsapp/routes.html')	

@login_required
def history(request):	
	return render(request, 'cmsapp/history.html')	

@login_required
def flot(request):	
	return render(request, 'cmsapp/flot.html')	

@login_required	
def morris(request):	
	return render(request, 'cmsapp/morris.html')	

@login_required
def forms(request):	
	return render(request, 'cmsapp/forms.html')	

@login_required
def panelswells(request):	
	return render(request, 'cmsapp/panelswells.html')	

@login_required
def buttons(request):	
	return render(request, 'cmsapp/buttons.html')	

@login_required
def notifications(request):	
	return render(request, 'cmsapp/notifications.html')	

@login_required
def typography(request):	
	return render(request, 'cmsapp/typography.html')	

@login_required
def icons(request):	
	return render(request, 'cmsapp/icons.html')	

@login_required
def grid(request):	
	return render(request, 'cmsapp/grid.html')	

@login_required
def blank(request):	
	return render(request, 'cmsapp/blank.html')

@login_required
def login(request):	
	return render(request, 'cmsapp/login.html')	
