# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'BuildStream'
SITENAME = 'BuildStream, the software integration tool'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

STATIC_PATHS = [
  '.well-known/acme-challenge',
]

import sys
sys.path.append('.')
from get_releases import DownloadTable

MARKDOWN = {
  'extensions': [
      DownloadTable()
  ],
  'extension_configs': {
    'markdown.extensions.toc': {
      'title': 'Table of contents:'
    },
    'markdown.extensions.extra': {}
  },
}

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Portfolio', '/pages/buildstream-portfolio.html'),
    ('Download', '/pages/download.html'),
    ('FAQ', '/pages/frequently-asked-questions.html'),
)
