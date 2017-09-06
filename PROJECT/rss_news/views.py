from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class MyIndex(TemplateView):
    template_name = 'index.html'

#def index(request):
#    return render(request,"index.html", context)