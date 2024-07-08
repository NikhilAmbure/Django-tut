from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hey, Welcome</h1>') 

    # Sending Dynamic data from views.py -->
    # name = 'Patrick'
    # context = {
        # 'name': 'Patrick',
        # 'age': 23,
        # 'nationality': 'British',
    # }
    # return render(request, 'index.html', context)


    # Building a word Counter 
    return render(request, 'index.html')


# Building a word Counter 
def counter(request):
    pass
    # words = request.GET['text']
    # words = request.POST['text']
    # amount_of_words = len(words.split())
    # return render(request, 'counter.html', {'amount': amount_of_words})