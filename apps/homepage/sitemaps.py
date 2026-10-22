from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class homepage_sitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'
    def items(self):
        return ['homepage:index']

    def location(self, item):
        # Resolve URL
        print(item)
        return reverse(item)