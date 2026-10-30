from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class HomeIndexSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'
    def items(self):
        return ['home:index', 'home:about', 'home:contact']

    def location(self, item):
        # Resolve URL
        return reverse(item)