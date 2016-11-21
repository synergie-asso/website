#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Synergie'
SITENAME = 'Synergie'
SITEURL = ''
DESCRIPTION = 'Agir en faveur de la diversité dans les métiers de l\'informatique'

PATH = 'content'
THEME = 'themes/synergie-monospace'

LOCALE = ("fr_FR")
TIMEZONE = 'Europe/Paris'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

# Content
USE_FOLDER_AS_CATEGORY = False

# Theme related
MD_EXTENSONS = ['codehilite(css_class=codehilite code)']
LOGO_SYNERGIE = "images/synergie_logo.png"
