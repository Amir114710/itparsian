from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import base as settings
from apps.account.views import Login, Register, activate

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('apps.mysite.urls')),  # ALL PAGES URL IN MYSITE APP
                  path('account/', include('apps.account.urls')),  # ADMIN PANEL AND REGISTRATION APP
                  path('blog/', include('apps.blog.urls')),  # ALL BLOG URL IN BLOG APP
                  path('ticket/', include('apps.ticket.urls')),  # CONTACT US URLS IN TICKET APP
                  path('login/', Login.as_view(), name='login'),
                  path('register/', Register.as_view(), name='register'),
                  path('activate/<uidb64>/<token>/', activate, name='activate'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
