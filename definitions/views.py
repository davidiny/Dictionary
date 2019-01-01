from django.shortcuts import render

# Create your views here.
import requests
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    form = MyForm(request.POST or None)
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            search = cd.get('word')
            resp = requests.get('http://api.wordnik.com/v4/word.json/{}/definitions?api_key=14b5420c184640c683005077d1008bba39ae0cd175d218830'.format(search))
            answer = resp.json
            return render(request, 'definition.html', {'form': form, 'word': answer[0]['word'], 'definition' : answer[0]['text'], 'partOfSpeech' : answer[0].get('partOfSpeech', "N/A")})
    else:
        form = MyForm(request.POST or None)
        resp = requests.get('http://api.wordnik.com/v4/words.json/wordOfTheDay?api_key=14b5420c184640c683005077d1008bba39ae0cd175d218830')
        answer = resp.json()
        # t = get_template('home.html')
        # html = t.render({'word' : answer['word'], 'definition' : answer['definitions'][0]['text'], 'partOfSpeech' : answer['definitions'][0]['partOfSpeech']})
        # for x in answer:
        #     print(x)
        # return HttpResponse(html)
    return render(request, 'home.html', {'form': form, 'word': answer['word'], 'definition' : answer['definitions'][0]['text'], 'partOfSpeech' : answer['definitions'][0].get('partOfSpeech', "N/A")})