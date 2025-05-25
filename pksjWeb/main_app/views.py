from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView
from django.urls import reverse
from .models import Paymentlist



# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def get_line_profile(request):
    try:
        social_account = SocialAccount.objects.get(user=request.user, provider='line')
        extra_data = social_account.extra_data
        return {
            'name': extra_data.get('name'),
            'picture': extra_data.get('picture'),
            'raw': extra_data,
        }
    except SocialAccount.DoesNotExist:
        return None

        

@login_required
def profile(request):
    profile = get_line_profile(request)
    payments = Paymentlist.objects.filter(user=request.user).order_by('-transfer_date')
    return render(request, 'main_app/profile.html', {'profile': profile , 'payments': payments})