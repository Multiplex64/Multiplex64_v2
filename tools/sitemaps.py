from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class tools_sitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'
    def items(self):
        return ['tools:index']

    def location(self, item):
        # Resolve URL
        print(item)
        return reverse(item)