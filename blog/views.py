from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from datetime import datetime
from .models import ArticleModel
from .forms import ArticleForm
from django.utils import timezone
from django.shortcuts import get_object_or_404


class Article(View):

    def get(self, request):
        form = ArticleForm()
        articles = ArticleModel.objects.all()
        context = {
            "articles": articles,
            "form": form,
        }
        return render(request, 'blog/articles.html', context)

    def post(self, request):
        # title = request.POST['title']
        # category = request.POST['category']
        # author = request.POST['author']
        # content = request.POST['content']
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.instance.created_at = datetime.now(tz=timezone.utc)
            form.save()
        # ArticleModel.objects.create(title=title, category=category, author=author, content=content)
        articles = ArticleModel.objects.all()
        form = ArticleForm()
        context = {
            "articles": articles,
            "form": form,
        }
        return render(request, 'blog/articles.html', context)


# def index(request):
#     if request.method == "GET":
#         return HttpResponse("Welcome GET to my blog!")
#     if request.method == "POST":
#         return HttpResponse("Welcome POST to my blog!")

class Home(View):
    def get(self, request):
        return HttpResponse("Welcome get to my blog!")

    def post(self, request):
        return HttpResponse("Welcome post to my blog!")


class ArticleDetails(View):
    def get(self, request, id):
        article = get_object_or_404(ArticleModel, id=id)
        context = {
            "article": article,
        }
        return render(request, "blog/article_details.html", context)

    # def post(self, request, id):
    #     return HttpResponse("Welcome post to my blog!")
