from django.shortcuts import render, redirect
from django.contrib import messages

def home_view(request):
    return render(request, 'core/home.html')

def program_view(request):
    return render(request, 'core/program.html')

def support_view(request):
    if request.method == 'POST':
        messages.success(request, "Your inquiry has been successfully logged! A Kriya coordinator will review your ticket and contact you shortly.")
        return redirect('core:support')
    return render(request, 'core/support.html')
