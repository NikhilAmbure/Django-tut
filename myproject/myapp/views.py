from django.shortcuts import render
from django.http import HttpResponse
# from .models import Feature
from .models import Features

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



    # Introduction to Models (Basics)
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.is_true = True
    # feature1.details = 'Quick Service'

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Reliable'
    # feature2.is_true = True
    # feature2.details = 'More reliable'

    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Easy to use'
    # feature3.is_true = False
    # feature3.details = 'Easy'

    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'Affordable'
    # feature4.is_true = True
    # feature4.details = 'Service Affordable' 

    # feature5 = Feature()
    # feature5.id = 4
    # feature5.name = 'TrustWorthy'
    # feature5.is_true = True
    # feature5.details = 'Service Trustable'

    # For more dynamic --> we can use list
    # features = [feature1, feature2, feature3, feature4, feature5]
    # return render(request, 'index.html', {'feature1': feature1, 'feature2':feature2, 'feature3': feature3, 'feature4':feature4})
    



    # Admin Panel and Manipulation of database
    features = Features.objects.all() 
    return render(request, 'index.html', {'features': features})


# Building a word Counter 
def counter(request):
    pass
    # words = request.GET['text']
    # words = request.POST['text']
    # amount_of_words = len(words.split())
    # return render(request, 'counter.html', {'amount': amount_of_words})