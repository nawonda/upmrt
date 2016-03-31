from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
	return render(request, 'dashboard/dashboard.html')
	
@login_required
def profile(request):
	return render(request, 'dashboard/profile.html')

@login_required
def routes(request):	
	return render(request, 'dashboard/routes.html')	

@login_required
def history(request):	
	return render(request, 'dashboard/history.html')	

@login_required
def flot(request):	
	return render(request, 'dashboard/flot.html')	

@login_required	
def morris(request):	
	return render(request, 'dashboard/morris.html')	

@login_required
def forms(request):	
	return render(request, 'dashboard/forms.html')	

@login_required
def panelswells(request):	
	return render(request, 'dashboard/panelswells.html')	

@login_required
def buttons(request):	
	return render(request, 'dashboard/buttons.html')	

@login_required
def notifications(request):	
	return render(request, 'dashboard/notifications.html')	

@login_required
def typography(request):	
	return render(request, 'dashboard/typography.html')	

@login_required
def icons(request):	
	return render(request, 'dashboard/icons.html')	

@login_required
def grid(request):	
	return render(request, 'dashboard/grid.html')	

@login_required
def blank(request):	
	return render(request, 'dashboard/blank.html')

@login_required
def login(request):	
	return render(request, 'dashboard/login.html')	
