from django.shortcuts import render,redirect
from gnews.consumer import Consumer
import requests
import json
from config_reader.config import Config
from logger.log import Log



def load_news(request):
    try:    
        nwarticles=None
        title = request.GET.get('title')        
        config=Config("configuration")
        config_data=config.get_config_data()        
        if title is not None:
            api_url=config_data["news_api"]+"?title="+title
        else:
            api_url=config_data["news_api"]
        response = requests.get(api_url)
        if response.status_code == 200:
            api_data = response.json()
            nwarticles=json.loads(api_data)
        context={'nwarticles':nwarticles}
        return render(request, 'news_loader/news_space.html',context)
    except Exception as e:
            log=Log("Logging")
            log.write(e)