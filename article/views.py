from django.shortcuts import render,redirect
from .models import *
# Create your views here.

# context processor
def categories(request):
    categories = Category.objects.all()
    return {
        'categories':categories,
    }
    


def index(request):
    all_articles = Article.objects.all()
    context = {
            'articles':all_articles
    }
    return render(request,'article/index.html',context)

def single_article(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article":article,
    }
    return render(request,'article/article.html',context)

def categorised_article(request,pk):
    if pk == 0:
        articles = Article.objects.all()
        context = {
            'articles' : articles,
            'category' : 'all',
        }
    else:
       
        category = Category.objects.get(pk=pk)
        articles = Article.objects.filter(category=category).all()

        context = {
            'articles' : articles,
            'category' : category,
        }

    return render(request,"article/categorised_article.html",context)

def delete(request,id):
    queryset = Article.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes')
