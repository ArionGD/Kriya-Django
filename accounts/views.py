from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import User

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Registration successful! Welcome to KRIYA, {user.username}.")
            
            # Redirect based on role
            if user.is_client_user():
                return redirect('dashboard:client_dashboard')
            elif user.is_worker_user():
                return redirect('dashboard:worker_dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        # If already logged in, redirect to respective dashboard
        user = request.user
        if user.is_manager_user():
            return redirect('dashboard:ngo_dashboard')
        elif user.is_client_user():
            return redirect('dashboard:client_dashboard')
        elif user.is_worker_user():
            return redirect('dashboard:worker_dashboard')
        return redirect('home')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Logged in successfully. Welcome back, {username}!")
                
                # Redirect based on role
                if user.is_manager_user():
                    return redirect('dashboard:ngo_dashboard')
                elif user.is_client_user():
                    return redirect('dashboard:client_dashboard')
                elif user.is_worker_user():
                    return redirect('dashboard:worker_dashboard')
                else:
                    return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logged out successfully.")
    return redirect('home')
