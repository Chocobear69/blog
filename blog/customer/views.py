import json

from django.contrib.auth import authenticate, login, logout
from rest_framework.views import View
from django.http import HttpResponse


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse(status=200)
        return HttpResponse(status=401)

    def post(self, request):
        data = json.loads(request.body)
        email = data["email"]
        password = data["password"]

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return HttpResponse(status=200)


class Logout(View):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
        return HttpResponse(200)
