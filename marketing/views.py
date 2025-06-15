from django.shortcuts import render
from django.shortcuts import render
# Create your views here.



def marketing_page(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/dashboard.html')
    else:
        return render(request, 'index.html')


def contact_page(request):
    return render(request,"contact.html")

def gallery(request):
    return render(request,"gallerys.html")

def store(request):
    return render(request,"store.html")