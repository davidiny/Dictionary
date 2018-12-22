from django.shortcuts import render

# Create your views here.
import requests
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(action):
    resp = requests.get('http://api.wordnik.com/v4/words.json/randomWord?api_key=14b5420c184640c683005077d1008bba39ae0cd175d218830')
    answer = resp.json()
    the_word = str(answer['word'])
    resp2 = requests.get('http://api.wordnik.com/v4/word.json/{}/definitions?api_key=14b5420c184640c683005077d1008bba39ae0cd175d218830'.format(the_word))
    answer2 = resp2.json()
    t = get_template('random.html')
    html = t.render({'word' : answer['word'], 'definition' : answer2[0]['text'], 'partOfSpeech' : answer2[0]['partOfSpeech']})
    for x in answer:
        print(x)
    return HttpResponse(html)