#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('/home/joon/Dropbox/blog')
import pelicanconf_common as common

lang = u'ko'

AUTHOR = common.AUTHOR
SITENAME = common.SITENAME
TIMEZONE = common.TIMEZONE

SITEURL = common.SITEURL.format(lang)
DEFAULT_LANG = lang

# Blogroll
LINKS =  (('English Version', 'http://blog.joonro.net/en/'),)
LINKS += common.LINKS

# Social widget
SOCIAL = common.SOCIAL

DEFAULT_PAGINATION = common.DEFAULT_PAGINATION

OUTPUT_PATH = '../output/{}/'.format(lang)
DISQUS_SITENAME = common.DISQUS_SITENAME
THEME = common.THEME

