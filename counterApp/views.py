from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html', { 'promenna': 'tohle je prvni hodnota',
                                        'promenna2': 'tohle je druha hodnota'})

def about(request):
    return HttpResponse('<h1>O nas<h1>')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for slovo in wordlist:
        if slovo in worddictionary:
            worddictionary[slovo] += 1
        else:
            worddictionary[slovo] = 1


    return render(request,'count.html', {'fulltext':fulltext,'worddict':worddictionary, 'delkalistu': len(wordlist)})

def about_view(request):
    return render(request,'about.html',{'pozdrav': 'Zdravim', 'mapa': 'odkaz na google mapy: '})
