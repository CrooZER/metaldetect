from email.policy import HTTP
from http.client import HTTPResponse

from django.shortcuts import render


def index(request):
    return render(request, 'templates/index.html')