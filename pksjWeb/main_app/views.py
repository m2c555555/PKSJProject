from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')


@login_required
def profile(request):
    return render(request, 'main_app/profile.html', {'user': request.user})