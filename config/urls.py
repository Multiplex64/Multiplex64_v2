"""
URL configuration for config project.

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
from django.contrib.sitemaps.views import sitemap
from apps.homepage.sitemaps import HomepageIndexSitemap
from apps.tools.sitemaps import ToolsIndexSitemap, ToolsPagesSitemap

import os

secret_dir = os.environ.get("SECRET_DIR", "null/")


def static_root(request, path):
    """
    Serves files from static/root/ during development
    """
    document_root = os.path.join(settings.BASE_DIR, "static_root/")

    try:
        return serve(request, path, document_root=document_root)
    except Http404:
        raise Http404("File not found.")


sitemaps = {
    "homepage": HomepageIndexSitemap,
    "tools-index": ToolsIndexSitemap,
    "tools": ToolsPagesSitemap,
}

urlpatterns = [
    # General Directories
    path("", include("apps.homepage.urls")),
    path("tools/", include("apps.tools.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    # System/secret directories
    path(secret_dir + "admin/", admin.site.urls),
    # Static file system, should be bypassed in production
    re_path(r"^(?P<path>[\w\-]+\.[a-zA-Z0-9]+)$", static_root),
]
