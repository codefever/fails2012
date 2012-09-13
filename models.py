#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
from google.appengine.ext import db

class Item(db.Model):
    name = db.StringProperty(required=True)
    state = db.StringProperty(required=True)
    jobs = db.StringListProperty()
    reason = db.TextProperty()
    post_date = db.StringProperty(required=True)
    end_date = db.StringProperty() #cannot set None and put. WTF!

    def __str__(self):
        return '<"%s" "%s" "%s">' %(self.name, self.state, self.post_date)

    def get_dict(self):
        d = {'name':self.name, 'state':self.state, 'jobs':self.jobs, 'reason':self.reason}
        d['post_date'] = str(self.post_date)
        if self.end_date:
            d['end_date'] = str(self.end_date)
        else:
            d['end_date'] = None
        return d