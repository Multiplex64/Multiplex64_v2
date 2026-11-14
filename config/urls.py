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

import os
from pathlib import Path
import environ
from django.conf import settings
from django.http import Http404
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.views.generic.base import RedirectView
from django.contrib.sitemaps.views import sitemap
from apps.home.sitemaps import HomeIndexSitemap, HomePagesSitemap
from apps.pricing.sitemaps import PricingIndexSitemap
from apps.tools.sitemaps import ToolsIndexSitemap, ToolsPagesSitemap
from apps.feedback.sitemaps import FeedbackIndexSitemap

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False)
)

SECRET_DIR = env("SECRET_DIR", cast=str)
ENVIRONMENT = env("ENV", cast=str)

def static_root(request, path):
    """
    Serves files from static/root/ during development
    """
    document_root = os.path.join(settings.BASE_DIR, "static_root/")

    try:
        return serve(request, path, document_root=document_root)
    except Http404:
        raise Http404("File not found.")


# Permanent redirects
redirect_redirects = {
    "future-plans": "/roadmap/",
    "text-repeater": "/tools/text-repeater/",
    "html-playground": "/tools/html-playground/",
    "base-converter": "/tools/base-converter/",
    "number-analyzer": "/tools/number-analyzer/",
    "text-effects": "/tools/text-effects/",
    "time-difference": "/tools/time-difference/",
}


sitemaps = {
    "home-index": HomeIndexSitemap,
    "home-pages": HomePagesSitemap,
    "tools-index": ToolsIndexSitemap,
    "tools-pages": ToolsPagesSitemap,
    "pricing-index": PricingIndexSitemap,
    "feedback-index": FeedbackIndexSitemap,
}

urlpatterns = [
    # General Directories
    path("", include("apps.home.urls")),
    path("tools/", include("apps.tools.urls")),
    path("feedback/", include("apps.feedback.urls")),
    path("pricing/", include("apps.pricing.urls")),
    # Sitemaps
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    # Permanent Redirects
    *[
        re_path(rf"^{old_path}/?$", RedirectView.as_view(url=new_path, permanent=True))
        for old_path, new_path in redirect_redirects.items()
    ],
    # System/secret directories
    path(str(SECRET_DIR) + "admin/", admin.site.urls),
]

if ENVIRONMENT == "dev":
    # Add static file serving at root in development server, disable in prod
    urlpatterns.append(re_path(r"^(?P<path>[\w\-]+\.[a-zA-Z0-9]+)$", static_root))
