from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('mysite.urls')),  # ALL PAGES URL IN MYSITE APP
                  path('account/', include('account.urls')),  # ADMIN PANEL AND REGISTRATION APP
                  path('blog/', include('blog.urls')),  # ALL BLOG URL IN BLOG APP
                  path('ticket/', include('ticket.urls')),  # CONTACT US URLS IN TICKET APP

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
