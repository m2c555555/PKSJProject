from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def home(request):
    print()
    message="id:%s, uasername:%s firstname:%s, lastname:%s"%(request.user.pk, request.user.username, request.user.first_name, request.user.last_name)
    now = datetime.datetime.now()
    html = "<html><body><p>It is now %s.</p><p>%s</p></body></html>" % (now,message)
    
    return HttpResponse(html)