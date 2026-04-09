from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from products.models import Product


class StaticViewSitemap(Sitemap):
    """
    Stores sitemap entries for the main public site pages.
    """

    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return [
            "home",
            "products",
        ]

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    """
    Stores sitemap entries for individual product detail pages.
    """

    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return Product.objects.all()
