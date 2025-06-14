from django.urls import path,include
from marketing.views import marketing_page,contact_page,gallery,store
urlpatterns = [
    path("",marketing_page,name="home"),
    path("contact",contact_page,name="contact"),
    path("gallerys",gallery,name= "gallery"),
    path("store",store,name= "store"),
]