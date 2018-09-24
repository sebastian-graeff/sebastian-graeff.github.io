#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sebastian Graeff'
SITENAME = 'Sebastian Graeff'

# Paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']

# Top menus
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

TIMEZONE = 'Africa/Johannesburg'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Visit my educational website', 'https://www.kids-world-travel-guide.com'),)

# Social widget
SOCIAL = (('Find me on Linkedin', 'https://www.linkedin.com/in/sebastian-graeff/'),
          ('Or visit my GitHub profile', 'https://github.com/sebastian-graeff'),)

DEFAULT_PAGINATION = 5

SITEURL = 'https://sebastian-graeff.github.io/staticsite'
RELATIVE_URLS = True

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

# for Tipue Search Plugin
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

MARKUP = ('md', 'ipynb', 'rmd', 'html')

IPYNB_SKIP_CSS=True

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.youtube',
    'liquid_tags.notebook',
    'liquid_tags.include_code',
    'render_math',
    'pelican-ipynb.markup',
    'tipue_search' ] 

I18N_TEMPLATES_LANG = 'en'

# Additional .css and .js files to customize markdown tables
CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'

STATIC_PATHS = [ 'extra' ]
EXTRA_HEADER = open('_nb_header.html').read()

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}