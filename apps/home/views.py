from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")

def about(request):
     return render(request, "home/about.html")

def contact(request):
     return render(request, "home/contact.html")

def roadmap(request):
     return render(request, "home/roadmap.html")