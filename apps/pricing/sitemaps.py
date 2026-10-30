from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class PricingIndexSitemap(Sitemap):
    priority = 0.3
    changefreq = 'weekly'
    def items(self):
        return ['pricing:index']

    def location(self, item):
        # Resolve URL
        return reverse(item)