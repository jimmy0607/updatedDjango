from django.shortcuts import render, redirect
from .models import Album, Tour, BandHistory, BandMember
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def homepage(request):
    """
    Renders the 'homepage.html' template. No input parameters are required.
    """
    return render(request, 'homepage.html')

def album_list(request):
    """
    Queries the database for all albums, orders them by release date, and renders the 'album_list.html' template with the list of albums passed as context data.
    """
    albums = Album.objects.all().order_by('release_date')
    return render(request, 'album_list.html', {'albums': albums})

def tour_list(request):
    """
    Queries the database for all tours and renders the 'tour_list.html' template with the list of tours passed as context data.
    """
    tours = Tour.objects.all()
    return render(request, 'tour_list.html', {'tours': tours})

def band_history(request):
    """
    Queries the database for all band history events and renders the 'band_history.html' template with the list of events passed as context data.
    """
    history = BandHistory.objects.all()
    return render(request, 'band_history.html', {'history': history})

def band_members(request):
    """
    Queries the database for all band members, orders them by year joined (if available), and renders the 'band_members.html' template with the list of members passed as context data.
    """
    members = BandMember.objects.all().order_by('year_joined')
    return render(request, 'band_members.html', {'members': members})

def register(request):
    """
    Renders the 'register.html' template with a UserCreationForm instance passed as context data. If the request method is POST, the view validates the form and creates a new user, logs the user in, and redirects to the homepage. If the form is invalid, it re-renders the form with the errors displayed.
    """
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
    """
    Renders the 'login.html' template. If the request method is POST, it attempts to authenticate the user with the provided credentials. If successful, logs the user in, displays a welcome message, and redirects to the homepage. If unsuccessful, displays an error message.
    """
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
    """
     Logs the user out and redirects to the homepage.
    """
    logout(request)
    return redirect('home')