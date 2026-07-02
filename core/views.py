from django.shortcuts import render, redirect
from django.contrib import messages

def home_view(request):
    return render(request, 'core/home.html')

def program_view(request):
    return render(request, 'core/program.html')

def support_view(request):
    if request.method == 'POST':
        messages.success(request, "Your query has been logged. A Kriya coordinator will review your inquiry or grievance and follow up within 24 hours.")
        return redirect('core:support')
    return render(request, 'core/support.html')

def help_guide_view(request):
    return render(request, 'core/help_guide.html')
