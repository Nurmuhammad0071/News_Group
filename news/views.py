from django.shortcuts import render
from .models import News


# Create your views here.
def index(request):
    news = News.object.all()
    context = {
        'news': news
    }
    return render(request, 'biznews/index.html', context)


def category(request):
    return render(request, 'biznews/category.html')
