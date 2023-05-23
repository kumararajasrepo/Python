from rest_framework.decorators import api_view
from rest_framework.response import Response
from gnews.consumer import Consumer
import json


@api_view(['GET'])
def get_news(request):
    title = request.GET.get('title')
    if title is None:
        title="India"
    obj=Consumer("gnews")    
    nwarticles=obj.news_compile(title)
    return Response(json.dumps([article.__dict__ for article in nwarticles]))