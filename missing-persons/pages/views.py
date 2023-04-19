from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.
def indexPageView(request):
    return render(request,'pages/index.html')

def faqPageView(request):
    return render(request, 'pages/faq.html')

def showPeoplePageView(request) :

    db_people = Person.objects.all() 

    context = {
            "data" : db_people
    }

    return render(request, 'pages/showPeople.html', context)   


def displayPersonPageView(request, id) :

    person = Person.objects.get(id=id)   

    context = {
            "data" : person
    }

    return render(request, 'pages/displayPerson.html', context)    
