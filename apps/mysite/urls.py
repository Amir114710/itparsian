from django.urls import path
from . import views





app_name = 'site'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact', views.ContactUsView.as_view(), name='home'),
    path('about', views.AboutUsView.as_view(), name='home'),
    path('website', views.WebsiteView.as_view(), name='website'),
    path('seo', views.SeoView.as_view(), name='seo'),
]

