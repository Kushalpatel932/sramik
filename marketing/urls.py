from django.urls import path,include
from marketing.views import marketing_page
urlpatterns = [
    path("",marketing_page,name="home")
]