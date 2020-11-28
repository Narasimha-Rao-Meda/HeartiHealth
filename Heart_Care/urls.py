from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name='home'),
	path('services', views.services, name='services'),
	path('doctors', views.doctors, name='doctors'),
	path('prediction-results', views.results, name='result'),
]