from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class PricingIndexSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'
    def items(self):
        return ['pricing:index']

    def location(self, item):
        # Resolve URL
        return reverse(item)