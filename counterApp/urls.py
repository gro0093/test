from django.urls import path
from . import views
urlpatterns = [
 path('', views.home, name=''),
 path('about/', views.about_view, name='about'),
 path('count/', views.count, name='countJmeno'),
]
