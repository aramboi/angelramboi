#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Angel Ramboi'
SITENAME = u'¬_¬'
SITEURL = 'http://localhost:8000'
FEED_DOMAIN = SITEURL
TAGLINE = 'They mostly come at night ... mostly!'

PATH = 'content'

TIMEZONE = 'Europe/Dublin'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 10

THEME = 'theme/pure-single/'
COVER_IMG_URL = 'images/alt-bg.png'
FAVICON_URL = 'images/alt-favicon.png'
PROFILE_IMG_URL = 'images/me.jpg'

MENUITEMS = [('Archive', 'archives.html'), ('About', 'about.html'), ]

SOCIAL = (
    ('twitter', 'https://twitter.com/angelramboi'),
    ('github', 'https://github.com/aramboi'),
    ('bitbucket', 'https://bitbucket.org/aramboi'),
    ('rss', 'http://altshiftkill.com/feeds/all.atom.xml'),
)

DISPLAY_PAGES_ON_MENU = False
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = PAGE_SAVE_AS = '{slug}.html'

RELATIVE_URLS = False
