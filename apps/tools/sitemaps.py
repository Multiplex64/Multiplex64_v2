from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class ToolsIndexSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'
    def items(self):
        return ['tools:index']

    def location(self, item):
        # Resolve URL
        print(item)
        return reverse(item)

class ToolsPagesSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
