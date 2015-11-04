from django.shortcuts import render
from django.http import Http404,HttpResponse
from func import robots as r
# Create your views here.
def home(request):
    return render(request, 'home.html')

def robots(request):
    val = '今天'
    if 'val' in request.GET:
        val = request.GET['val']
        if len(val)!=0:
            info = r.getdata(val)
        else:
            info='不知道您在说什么'
    return HttpResponse(info)

