#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import json

from models import *
from settings import *

class Index(webapp2.RequestHandler):
    def get(self):
        q = Item.all().order('-end_date').fetch(limit=100)
        template = jinja_env.get_template('index.html')
        vars = {'title': TITLE,
                'items': q,
                'arthor': AUTHOR,
                'arthor_link': AUTHOR_LINK,
            }
        self.response.out.write(template.render(vars))

class Damn(webapp2.RequestHandler):
    def get(self):
        key = self.request.get('key', None)
        if not key:
            return self.error(500)
        e = db.get(key)
        if not e:
            return self.error(500)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(e.get_dict()))

class NotFound(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('404.html')
        vars = {'title': TITLE,
                'arthor': AUTHOR,
                'arthor_link': AUTHOR_LINK,
            }
        self.response.out.write(template.render(vars))

app = webapp2.WSGIApplication([('/', Index), ('/damn/', Damn), ('/.*', NotFound)], debug=DEBUG)
