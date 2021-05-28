from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'gen/home.html',)

def art(request):
    import random
    characters = list('abcde')

    length = 5

    thepassword =''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'gen/art.html', {'password':thepassword})

def about(request):
    return render(request,'gen/about.html',)    
