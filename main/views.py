# from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
# from django.conf import settings
# from django import forms
# from django.contrib.auth.decorators import login_required

from .models import *
from django.views.generic import View

# class AjaxHandlerView(View):
#     def get(self, request):
#         text = request.GET.get("button_text")
#         if (request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'):
#             t = time()
#             return JsonResponse({'seconds': t},status=200)
#         return render(request, 'index.html')

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def projects(request):
    return render(request, "main/projects.html",{
        "projects" : Project.objects.all()
    })

def contact(request):
    return render(request, "main/contact.html")