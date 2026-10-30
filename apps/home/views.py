from django.shortcuts import render


def index(request):
    return render(request, "home/index.html", {"base_template": "base.html"})

def about(request):
     return render(request, "home/about.html", {"base_template": "base.html"})

def contact(request):
     return render(request, "home/contact.html", {"base_template": "base.html"})