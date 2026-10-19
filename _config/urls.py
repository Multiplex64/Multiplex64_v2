"""
URL configuration for _config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.http import Http404
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
import os


def static_root(request, path):
    """
    Serves files from _static/root/ during development
    """
    document_root = os.path.join(settings.BASE_DIR, "_static_root/")

    try:
        return serve(request, path, document_root=document_root)
    except Http404:
        raise Http404("File not found at root.")


urlpatterns = [
    path("api/administration/", admin.site.urls),
    path("", include("homepage.urls")),
    # static file system, should be bypassed in production
    re_path(
        r"^static/(?P<path>[\w\-]+\.[a-zA-Z0-9]+)$",
        serve,
        {"document_root": settings.BASE_DIR / "_static"},
    ),
    re_path(r"^(?P<path>[\w\-]+\.[a-zA-Z0-9]+)$", static_root),
]
