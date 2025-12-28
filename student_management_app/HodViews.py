from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


def admin_home(request):
    return HttpResponse('Hello, admin Page!')
