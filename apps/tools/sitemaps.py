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
        # Auto-generate tools pages in sitemap based on the files in templates/

        template_dir = os.path.join(
            settings.BASE_DIR, "apps", "tools", "templates", "tools"
        )

        template_urls = []
        if os.path.exists(template_dir):
            for root, dirs, files in os.walk(template_dir):
                for file in files:
                    if file.endswith(".html") and file != "index.html":
                        view_name = f"tools:{file.replace('.html', '')}"
                        print(view_name)
                        try:
                            reverse(
                                "tools:tool",
                                kwargs={"template_name": view_name.rpartition(":")[2]},
                            )
                            template_urls.append(view_name)
                        except NoReverseMatch:
                            pass
        return template_urls

    def location(self, item):
        # Resolve URL
        return reverse("tools:tool", kwargs={"template_name": item.rpartition(":")[2]})
