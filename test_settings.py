DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'portfolio.context_processors.collections',
    'portfolio.context_processors.artworks',
    'portfolio.context_processors.categories'
)

INSTALLED_APPS = [
    'django.contrib.sitemaps',
    'sorl.thumbnail',
    'adminsortable',
    'portfolio'
]

try:
    # If available, South is required by setuptest
    import south
    INSTALLED_APPS.append('south')
except ImportError:
    # South not installed and hence is not required
    pass

ROOT_URLCONF = 'test_urls'

SITE_ID = 1
