from django.shortcuts import render

# Create your views here.
from django.conf import settings
from urllib.parse import urlencode
import requests
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User

def google_login(request):
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    params = {
        "client_id":settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        "redirect_uri":request.build_absolute_uri("/auth/callback/"),
        "response_type":"code",
        "scope":" ".join(settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE),
        "access_type":"offline"
    }
    auth_url = f"{base_url}?{urlencode(params)}"
    return redirect(auth_url)


def google_auth_callback(request):
    code = request.GET.get('code')

    if not code:
        return JsonResponse({"error":"Authorization failed"},status = 400)
    token_url = 'https://oauth2.googleapis.com/token'
    data = {
        'code': code,
        'client_id': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        'client_secret': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
        'redirect_uri': request.build_absolute_uri('/auth/callback/'),
        'grant_type': 'authorization_code',
    }

    response = requests.post(token_url, data=data)
    token_data = response.json()
    access_token = token_data.get("access_token")
    user_info_response = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    user_info = user_info_response.json()
    email = user_info.get("email")
    name = user_info.get("name", "")
    user, created = User.objects.get_or_create(username=email, defaults={"first_name": name, "email": email})
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

    return redirect("/")
    

    # return JsonResponse({"success": True,"token_data":token_data})
    
