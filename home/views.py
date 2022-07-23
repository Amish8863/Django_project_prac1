from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        "variable1": "sent",
        "variable2": "My name is Amish singh"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is our homepage")

def about(request):
    return HttpResponse("this is our aboutpage")

def services(request):
    return HttpResponse("this is our servicespage")


def contact(request):
    return HttpResponse("this is our contactpage")

