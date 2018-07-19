from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from core.settings import BASE_DIR
from myblog import models

import plotly
from plotly import graph_objs as go




# Create your views here.
@csrf_exempt
def home(request):
  # return render(request, 'home.html', {})
  return render(request, 'home.html', {}) 
  
# introduction view
def introduction(request, name):
	return render(request, 'in/%s.html'%name, {})

# blog view
def blog(request, name, article_num):
	return render(request, 'blog/%s/%d.html'%(name, article_num))