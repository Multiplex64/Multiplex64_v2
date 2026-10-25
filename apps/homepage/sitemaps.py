from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class HomepageIndexSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'
    def items(self):
        return ['homepage:index']

    def location(self, item):
        # Resolve URL
        return reverse(item)