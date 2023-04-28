from django.shortcuts import render, redirect
from .models import Album, Tour, BandHistory, BandMember
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def homepage(request):
    return render(request, 'homepage.html')

def album_list(request):
    albums = Album.objects.all().order_by('release_date')
    return render(request, 'album_list.html', {'albums': albums})

def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'tour_list.html', {'tours': tours})

def band_history(request):
    history = BandHistory.objects.all()
    return render(request, 'band_history.html', {'history': history})

def band_members(request):
    members = BandMember.objects.all().order_by('year_joined')
    return render(request, 'band_members.html', {'members': members})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    return redirect('home')