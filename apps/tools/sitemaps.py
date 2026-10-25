import os
from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.urls import reverse, NoReverseMatch


class ToolsIndexSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return ["tools:index"]

    def location(self, item):
        # Resolve URL
        return reverse(item)


class ToolsPagesSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        # Define your templates folder path
        template_dir = os.path.join(
            settings.BASE_DIR, "apps", "tools", "templates", "tools"
        )

        template_urls = []
        if os.path.exists(template_dir):
            for root, dirs, files in os.walk(template_dir):
                for file in files:
                    if file.endswith(".html"):
                        # Map file name to a named URL pattern or build a path
                        # Example: assuming file 'about.html' maps to view name 'myapp:about'
                        view_name = f"tools:{file.replace('.html', '')}"
                        print(view_name)
                        try:
                            template_urls.append(view_name)
                        except NoReverseMatch:
                            pass
        return template_urls

    def location(self, item):
        # Resolve URL
        return f"/tools/{item.rpartition(":")[2]}/"