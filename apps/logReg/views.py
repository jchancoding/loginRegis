# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt

def index(request):
    return render(request, 'logReg/index.html')

def registration(request):
    errors = users.objects.reg_validator(request.POST)
    hashedpw = bcrypt.hashpw(request.POST['pw1'].encode(), bcrypt.gensalt())

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user = users.objects.create(f_name=request.POST['f_name'], l_name=request.POST['l_name'], email=request.POST['email'], pw=hashedpw)
        user.save()
        request.session['f_name'] = user.f_name
        return redirect('/success')

def login(request):

    log_email = request.POST['email']
    errors = users.objects.log_validator(request.POST)
    print errors
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        request.session['f_name'] = users.objects.get(email=log_email).f_name
        request.session['l_name'] = users.objects.get(email=log_email).l_name
        request.session['email'] = users.objects.get(email=log_email).email
        return redirect("/success")

def success(request):
    context = {
    "f_name": request.session['f_name']
    }
    return render(request, 'logReg/success.html', context)

def delete(request):
    email = request.session['email']
    users.objects.filter(email=email).delete()
    messages.success(request, 'Deleted yourself')
    return redirect('/')
