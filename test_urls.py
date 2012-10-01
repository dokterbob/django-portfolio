from django.conf.urls import patterns, include

from portfolio.sitemaps import portfolio_sitemaps as sitemaps


urlpatterns = patterns('',
    (r'^portfolio/', include('portfolio.urls')),

    # Sitemaps
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
)
