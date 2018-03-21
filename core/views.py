from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
#Import Personales

#@login_required
def home(request):
    return render(request, 'home.html', { })

def faq(request):
    return render(request, 'faq.html', { })