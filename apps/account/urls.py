from django.contrib.auth import views
from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    
    path('', views.ArticleList.as_view(), name='home'),
    path('article/create', views.ArticleCreate.as_view(), name='article-create'),
    path('article/update/<int:pk>', views.ArticleUpdate.as_view(), name='article-update'),
    path('article/delete/<int:pk>', views.DeleteArticle.as_view(), name='article-delete'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('ticket/list', views.TicketListView.as_view(), name='ticket'),
    path('ticket/delete/<int:pk>', views.DeleteTicket.as_view(), name='ticket-delete'),

]