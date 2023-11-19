from django.core.cache import cache
from django.shortcuts import render
from .models import News

def index(request):
    # Try from cache
    cached_data = cache.get('news_data')
    print('From cache')

    # From Database
    if cached_data is None:
        news_data = News.objects.all() 
        print('From database')
        cache.set('news_data', news_data, timeout=3600)
    else:
        news_data = cached_data

    return render(request, 'index.html', 
                  {'news_data': news_data}
                  )
