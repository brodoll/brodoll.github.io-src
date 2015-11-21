#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Guilherme Pedrosa'
SITENAME = u'Guilherme Pedrosa'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Recife'

DEFAULT_LANG = u'en'

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

# Feeds 
#FEEDS =  (('All posts', 'feeds/all.atom.xml'),
#          ('Coding', 'feeds/category/coding.atom.xml'),
#          ('Event', 'feeds/category/event.atom.xml'),
#          ('Misc', 'feeds/category/misc.atom.xml'),
#          ('OPW', 'feeds/tag/opw.atom.xml'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/brodoll'),
          ('Twitter', 'https://twitter.com/gtpedrosa'),
          ('Linkedin', 'https://br.linkedin.com/in/guilherme-pedrosa-73213aa0'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Formatting for dates

DEFAULT_DATE_FORMAT = ('%a %d %B %Y')

# Formatting for urls

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first

NEWEST_FIRST_ARCHIVES = False

# Tell Pelican about directories

STATIC_PATHS = ['images', 'code']

# Specify theme
THEME = "/home/guilherme/pelican/pelican-themes/tuxlite_tbs"

# Plugins
PLUGIN_PATH = '/home/guilherme/pelican/pelican-plugins'
PLUGINS = ['latex', 'neighbors', 'summary']

# Only use LaTeX for selected articles

LATEX = 'article'
