from django.views.generic import ListView, TemplateView
from .models import ProjectDone, ContentBox, Services , TipsAbout
from apps.blog.models import Article
from django.shortcuts import render
# Create your views here.

class HomeView(ListView):
    template_name = 'mysite/index.html'
    context_object_name = 'object'

    def get_queryset(self):
        context = {
            'tip' : TipsAbout.objects.all(),
            'project': ProjectDone.objects.all(),
            'content': ContentBox.objects.all(),
            'services': Services.objects.all(),
            'recent_articles': Article.objects.filter(status="p").order_by('-publish')[0:4]
        }
        return context

class AboutUsView(TemplateView):
    template_name = 'mysite/about-us.html'


class ContactUsView(TemplateView):
    template_name = 'mysite/contact-us.html'





