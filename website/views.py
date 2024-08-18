from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all() 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Anda sudah login")
            return redirect('home')
        else:
            messages.error(request, "Username atau password salah, coba lagi")
            return redirect('home')
    return render(request, 'home.html', {'records':records})

def login_user(request):
    # Implementation for login_user, if needed
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Anda berhasil logout")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Anda berhasil mendaftar")
                return redirect('home')
        else:
            messages.error(request, "Ada kesalahan dalam formulir. Silakan coba lagi.")
    else:
        form = SignUpForm()  
    return render(request, 'register.html', {'form': form})

def record_perangkat(request, nama_desa):
    if request.user.is_authenticated:
        record_perangkat = Record.objects.get(desa=nama_desa)
        return render(request, 'record.html', {'record_perangkat': record_perangkat})
    else:
         messages.success(request, "Anda telah Log In")
         return redirect('home')