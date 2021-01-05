# -*- coding: utf-8 -*- #
import sys

AUTHOR = 'BuildStream'
SITENAME = 'BuildStream, the software integration tool'
SITEIMAGE = '/site-logo/BuildStream-logo-emblem-blue.png width=140 height=140'
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
    'images',
    'site-logo/BuildStream-logo-emblem-blue.png'
]

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

THEME = 'alchemy-theme/alchemy'
DEFAULT_PAGINATION = 10

MENUITEMS = (
    ('Install', 'install.html'),
    ('Documentation&#8599', 'https://docs.buildstream.build'),
    ('Source&#8599', 'https://github.com/apache/buildstream'),
    ('Contributing&#8599', 'https://github.com/apache/buildstream/tree/master/CONTRIBUTING.rst'),
    ('Mailing List&#8599', 'https://lists.apache.org/list.html?dev@buildstream.apache.org'),
    ('IRC&#8599', 'irc://irc.gnome.org/#buildstream'),
    ('News', 'news.html'),
)

MARKDOWN = {
    'extensions': [
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
