#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from google.appengine.api import users

from models import *
from settings import *

class Admin(webapp2.RequestHandler):
    def get(self):
        items = Item.all().order('-post_date').fetch(1000)
        username = users.get_current_user().nickname()
        logout_url = users.create_logout_url('/')
        vars = {'items': items,
                'title': TITLE,
                'username': username,
                'logout_url': logout_url}
        template = jinja_env.get_template('admin.html')
        self.response.out.write(template.render(vars))

    def post(self):
        dels = self.request.get_all('select-del')
        if len(dels) > 0:
            db.delete(dels)
        self.redirect('/admin-x/')

@db.transactional
def delete_items(key):
    db.delete(key)

class ItemPage(webapp2.RequestHandler):
    def get(self):
        key = self.request.get('k', None)
        template = jinja_env.get_template('item.html')
        vars = {'title': TITLE, 'e': None}
        if key:
            e = db.get(key)
            if e:
                vars['e'] = e
        self.response.out.write(template.render(vars))

    def post(self):
        key = self.request.get('k', None)
#       Get post data
        name = self.request.get('name', None)
        state = self.request.get('state', None)
        jobs = self.request.get('jobs', '')
        reason = self.request.get('reason', '')
        post_date = self.request.get('post-date', '')
        end_date = self.request.get('end-date', '')
#       Normalize
        if jobs:
            jobs = jobs.split(',')
        else:
            jobs = []
        if post_date:
            post_date = str(date(*[int(v) for v in post_date.split('-')]))
        if end_date:
            end_date = str(date(*[int(v) for v in end_date.split('-')]))

        if not key:
            e = Item(name=name, state=state, post_date=post_date, jobs=jobs, reason=reason, end_date=end_date)
        else:
            e = db.get(key)
            e.name = name
            e.state = state
            e.jobs = jobs
            e.reason = reason
            e.post_date = post_date
            e.end_date = end_date
        e.put()
        self.redirect('/admin-x/')

app = webapp2.WSGIApplication([('/admin-x/?', Admin), ('/admin-x/item/', ItemPage)], debug=DEBUG)
