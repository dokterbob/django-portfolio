django-portfolio
================

.. image:: https://secure.travis-ci.org/dokterbob/django-portfolio.png
    :target: http://travis-ci.org/dokterbob/django-portfolio

An artist's portfolio as a pluggable Django app.

Installation
------------
1. `pip install -e https://github.com/dokterbob/django-portfolio.git#egg=django-portfolio`
2. Follow `sorl-thumbnail's installation instructions <http://sorl-thumbnail.readthedocs.org/en/latest/installation.html#setup>`_.
3. Follow `django-admin-sortable's installation instructions <http://pypi.python.org/pypi/django-admin-sortable/>`_.
4. Add `portfolio` to `INSTALLED_APPS`.
5. Include URL's into Django's URL space, like such::

        urlpatterns = patterns('',
            (r'^portfolio/', include('portfolio.urls')),
            ...
        )

6. Done! Have a cup of coffee!

7. Copy the minimal base templates from the `templates folder <https://github.com/dokterbob/django-portfolio/tree/master/portfolio/templates>`_ to your project's template
   folder and start customizing.
