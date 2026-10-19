from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world! Welcome to a new chapter for Multiplex64.")