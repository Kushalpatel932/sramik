from django.shortcuts import render
from django.shortcuts import render
# Create your views here.



def marketing_page(request):
    return render(request,'index.html')