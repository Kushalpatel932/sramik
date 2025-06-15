from django.urls import path,include
from auth2.views import google_login, google_auth_callback
urlpatterns = [
    path("login/",google_login,name="google_login"),
    path("callback/",google_auth_callback,name="call_back")
    
]