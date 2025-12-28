
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


def student_home(request):
    return HttpResponse('Hello, student Page!')