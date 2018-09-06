# -*- coding: utf-8 -*- #
import sys

sys.path.append('.')
from get_releases import DownloadTable

AUTHOR = 'BuildStream'
SITENAME = 'BuildStream, the software integration tool'
SITEURL = ''
RELATIVE_URLS = True

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
ARTICLE_URL = 'articles/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}/index.html'
INDEX_SAVE_AS = 'news.html'
STATIC_PATHS = [
    '.well-known/acme-challenge',
    'favicon.ico',
]

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

THEME = 'alchemy-theme/alchemy'
DEFAULT_PAGINATION = 10

MENUITEMS = (
    ('About', 'about.html'),
    ('Install', 'install.html'),
    ('News', 'news.html'),
    ('Community', 'community.html'),
    ('FAQ', 'faq.html'),
)

MARKDOWN = {
    'extensions': [
        DownloadTable(),
        'markdown.extensions.toc',
        'markdown.extensions.extra',
        'markdown.extensions.codehilite'
    ],
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        }
    },
}

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
