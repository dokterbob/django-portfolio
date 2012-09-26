DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'portfolio.context_processors.collections',
    'portfolio.context_processors.artworks'
)

INSTALLED_APPS = (
    'sorl.thumbnail',
    'portfolio'
)

ROOT_URLCONF = 'test_urls'

SITE_ID = 1
