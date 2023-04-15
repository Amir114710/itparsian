from django.urls import path
from .views import HomeView, AboutUsView, ContactUsView





app_name = 'site'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact', ContactUsView.as_view(), name='home'),
    path('about', AboutUsView.as_view(), name='home'),
]

