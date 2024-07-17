import sys
sys.path.append('.')

AUTHOR = 'dydev012'
SITENAME = 'notes'

SITEURL = "https://dydev012.github.io"

PATH = "content"
THEME = './themes/mg-theme'

TIMEZONE = 'GB'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = False

# Social widget
SOCIAL = (
            ('github', 'https://github.com/dydev012'),
            ('envelope', 'mailto:dydev012@gmail.com'),)

SUMMARY_MAX_LENGTH = 0 # Above
SUBSUMMARY_MAX_LENGTH = 100 # Below
SUMMARY_END_SUFFIX = '…'
DEFAULT_PAGINATION = False

# https://github.com/pelican-plugins/render-math?tab=readme-ov-file#settings
MATH_JAX = {
'align': 'center',
'auto_insert': True,
'indent': '0em',
'show_menu': True,
'process_escapes': True,
'MathJax_font': 'default',
'latex_preview': 'Tex',
'color': 'inherit',
'linebreak_automatic': False,
'tex_extensions': [],
'responsive': False,
'responsive_break': 768,
'process_summary': False,
'message_style': 'normal'
}

# enable search within theme
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'tags', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
TAGS_SAVE_AS = 'tags.html'

# Uncomment following line if you want doscument-relative URLs when developing
# RELATIVE_URLS = True

from filters import *

def generate_summary(content):
    # if in markup form
    nojax_text = clean_mathjax_markup(content)
    nojax_text = ' '.join(clean_mathjax(nojax_text).split(' ')[:SUBSUMMARY_MAX_LENGTH])
    nojax_text = nojax_text.rstrip()
    return nojax_text

JINJA_FILTERS = {
    'generate_summary': generate_summary,
    'category2url': name2slug,
    'title2url': title2url,
    'rm_html_suffix': rm_html_suffix
}
