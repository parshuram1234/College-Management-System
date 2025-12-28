from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


def staff_home(request):
    # Fetching All Students under Staff
    return render(request, "Hello, Staff Home Page")
