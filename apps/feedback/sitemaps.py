from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class FeedbackIndexSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'
    def items(self):
        return ['feedback:index']

    def location(self, item):
        # Resolve URL
        return reverse(item)