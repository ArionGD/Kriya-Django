from django.shortcuts import render, redirect
from django.contrib import messages

def home_view(request):
    return render(request, 'core/home.html')

def features_view(request):
    return render(request, 'core/features.html')

def support_view(request):
    if request.method == 'POST':
        messages.success(request, "Your message has been received! Our coordination team will get back to you shortly.")
        return redirect('core:support')
    return render(request, 'core/support.html')

def help_guide_view(request):
    return render(request, 'core/help_guide.html')
