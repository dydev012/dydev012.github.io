import sys
sys.path.append('.')
from env import theme_path

AUTHOR = 'dydev012'
SITENAME = 'notes et al.'
SITEURL = "https://dydev012.github.io"

PATH = "content"

TIMEZONE = 'GB'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
            ('github', 'https://github.com/dydev012'),
            ('envelope', 'mailto:dydev012@gmail.com'),)

DEFAULT_PAGINATION = 5

THEME = theme_path
# enable search within theme
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'
# Uncomment following line if you want doscument-relative URLs when developing
# RELATIVE_URLS = True