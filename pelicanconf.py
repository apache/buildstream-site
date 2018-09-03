# -*- coding: utf-8 -*- #
import sys

sys.path.append('.')
from get_releases import DownloadTable

AUTHOR = 'BuildStream'
SITENAME = 'BuildStream, the software integration tool'
SITEURL = ''

ARTICLE_URL = 'articles/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}/index.html'
INDEX_SAVE_AS = 'updates.html'
STATIC_PATHS = [
    '.well-known/acme-challenge',
]

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

THEME = 'theme'
DEFAULT_PAGINATION = 10

MENUITEMS = (
    ('Portfolio', '/portfolio.html'),
    ('Download', '/download.html'),
    ('Updates', '/updates.html'),
    ('Community', '/community.html'),
    ('FAQ', '/faq.html'),
)

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

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
