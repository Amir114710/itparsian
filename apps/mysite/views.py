from django.views.generic import ListView
from .models import ProjectDone, ContentBox, Services
from apps.blog.models import Article
# Create your views here.

class HomeView(ListView):
    template_name = 'mysite/index.html'
    context_object_name = 'object'

    def get_queryset(self):
        context = {
            'project': ProjectDone.objects.all(),
            'content': ContentBox.objects.all(),
            'services': Services.objects.all(),
            'recent_articles': Article.objects.filter(status="p").order_by('-publish')[0:4]
        }
        return context
