from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.homepage, name='home'),
    path('albums/', views.album_list, name='album_list'),
    path('tours/', views.tour_list, name='tour_list'),
    path('bandhistory/', views.band_history, name='band_history'),
    path('bandmembers/', views.band_members, name='band_members'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout'),
    
]