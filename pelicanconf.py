#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sebastian Graeff'
SITENAME = 'Sebastian Graeff'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Johannesburg'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

IGNORE_FILES = ['.ipynb_checkpoints']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Edit to use theme
PLUGIN_PATHS = ['pelican-plugins']

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'


JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.youtube',
    'liquid_tags.notebook',
    'liquid_tags.include_code',
    'render_math',
    'pelican-ipynb.markup' ] 

I18N_TEMPLATES_LANG = 'en'

