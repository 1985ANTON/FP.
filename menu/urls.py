from django.contrib import admin
from django.urls import path
from menu import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Ensure this line is included only once
    path('', views.home, name='home'),
    path('add_coffee/', views.add_coffee, name='add_coffee'),
    path('add_snack/', views.add_snack, name='add_snack'),
]
