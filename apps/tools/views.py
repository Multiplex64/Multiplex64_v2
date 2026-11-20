from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.http import Http404


def index(request):
    return render(request, "tools/index.html")


def tool(request, template_name):
    if template_name == "index":
        raise Http404("Template does not exist")

    full_path = f"tools/{template_name}.html"

    try:
        return render(request, full_path)
    except TemplateDoesNotExist:
        raise Http404("Template does not exist")
