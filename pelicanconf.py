#!/usr/bin/env python3

PATH = 'content'

AUTHOR = 'Angel Ramboi'
SITENAME = "Angel Ramboi's Blog"
TAGLINE = 'coder, gamer, geek'
SITEURL = 'http://localhost:8000'
FEED_DOMAIN = SITEURL

TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# DELETE_OUTPUT_DIRECTORY = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
CATEGORIES_ORDER_BY = 'alphabetic'
TAGS_ORDER_BY = 'alphabetic'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
# YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'
# MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/{date:%m}/index.html'

# Theme settings
THEME = 'themes/brutalist/'
# Used for OG tags and Twitter Card data on index page
SITEIMAGE = 'alt-bg.png'
# Used for OG tags and Twitter Card data of index page
SITEDESCRIPTION = 'Personal blog, projects and opinions'
# path to favicon
FAVICON = 'profile-sm.jpg'
# path to logo for nav menu (optional)
# LOGO = 'profile-pic.jpg'
# first name for nav menu if logo isn't provided
FIRST_NAME = 'Angel'
# Twitter username for Twitter Card data
TWITTER_USERNAME = '@angelramboi'
# Toggle display of theme attribution in the footer (scroll down and see)
# Attribution is appreciated but totally fine to turn off!
ATTRIBUTION = False
# Social icons in footer
TWITTER = 'https://twitter.com/angelramboi'
GITHUB = 'https://github.com/aramboi'
LINKEDIN = 'https://www.linkedin.com/in/aramboi'
# Gravatar
GRAVATAR = 'https://secure.gravatar.com/avatar/f03910605400a038f8a874cb3e5dc10b?s=256'

MENUITEMS = [
    # ('categories', '/categories'),
    # ('tags', '/tags'),
    # ('rss', '/feeds/all.atom.xml'),
    # ('archive', '/archives.html'),
    # ('about', '/pages/about.html'),
]

PLUGIN_PATHS = ['plugins', ]
PLUGINS = [
    'sitemap',
    'category_order',
    # 'w3c_validate',
    'optimize_images',
    # 'gzip_cache'
]

# SITEMAP PLUGIN
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.9,
        'pages': 0.5,
        'indexes': 0.5,
    },
    'changefreqs': {
        'articles': 'weekly',
        'pages': 'yearly',
        'indexes': 'weekly',
    },
}
