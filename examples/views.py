import requests
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(action):
    resp = requests.get('http://api.wordnik.com/v4/words.json/wordOfTheDay?api_key=14b5420c184640c683005077d1008bba39ae0cd175d218830')
    answer = resp.json()
    t = get_template('definition.html')
    html = t.render({'word' : answer['word'], 'definition' : answer['definitions'][0]['text'], 'partOfSpeech' : answer['definitions'][0]['partOfSpeech']})
    for x in answer:
        print(x)
    return HttpResponse(html)