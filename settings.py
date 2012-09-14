#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jinja2
import os

DEBUG = True

TITLE = u'2012，Nelson应聘实习の黑历史'
AUTHOR = u'Nelson Liao'
AUTHOR_LINK = u'http://blog.nelson10.info'

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+'/templates'))
