from apps.account.models import User
from django.views.generic import ListView, DetailView , TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article, Category , Comment, Favorite
from apps.account.mixins import AuthoAccessMixin
from django.core.paginator import Paginator
from django.http import JsonResponse

class ArticleList(ListView):
    model = Article
    template_name = 'blog/blog.html'
    queryset = Article.objects.published()
    paginate_by = 10

class ArticleDetail(DetailView):
    template_name = 'blog/detail.html'
    model = Article
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = get_object_or_404(Article , slug=self.object.slug)
        article.save()
        context['suggested_videos'] = Article.objects.all()[:3]
        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
             article.hits.add(ip_address)
        if self.request.user.is_authenticated == True:
            if self.request.user.favorites.filter(article__title = self.object.title , user_id = self.request.user.id).exists():
                context['is_liked'] = True
            else:
                context['is_liked'] = False
        else:
            pass
        return context
    
    def post(self,request,slug):
        article = get_object_or_404(Article.objects.published(), slug=slug)
        user = request.POST.get('name')
        email = request.POST.get('email')
        parent_id = request.POST.get('parent_id')
        message = request.POST.get('message')
        Comment.objects.create(message=message, parent_id=parent_id , articles=article , users=user , email=email)
        return redirect('blog:detail' , slug)

def like(request , slug , pk):
    try:
        like = Favorite.objects.get(article__slug = slug , user_id=request.user.id)
        like.delete()
    except:
        Favorite.objects.create(article_id=pk , user_id = request.user.id)
    return redirect('blog:detail' , slug)

class ArticlePre(AuthoAccessMixin, DetailView):
    template_name = 'blog/detail.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)


class SearchBox(TemplateView):
    queryset = None
    template_name = 'blog/blog.html'
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        queryset = Article.objects.filter(title__icontains = q)
        page_number = request.GET.get('page')
        paginator = Paginator(queryset , 10)
        objects = paginator.get_page(page_number)
        return render(request, self.template_name, {'object_list': objects})


# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     articles_list = category.articles.published()

#     paginator = Paginator(articles_list, 4)
#     articles = paginator.get_page(page)
#     context = {
#         "category": category,
#         "article": articles,
#     }
#     return render(request, 'blog/category.html', context)
class CategoryList(ListView):
    template_name = "blog/category.html"
    paginate_by = 5
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class AuthorList(ListView):
    template_name = "blog/author.html"
    paginate_by = 5
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
