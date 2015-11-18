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

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

try:
    # If available, South is required by setuptest
    import south
    INSTALLED_APPS.append('south')
except ImportError:
    # South not installed and hence is not required
    pass

ROOT_URLCONF = 'tests.urls'

SITE_ID = 1

# Random secret key
import random
key_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = ''.join([
    random.SystemRandom().choice(key_chars) for i in range(50)
])
