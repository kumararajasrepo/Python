from news_api.views import get_news
from django.urls import path


urlpatterns = [
    path('get_news/',get_news),
]