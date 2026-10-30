from django.shortcuts import render


def index(request):
    return render(request, "pricing/index.html", {"base_template": "base.html"})