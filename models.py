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

#create_one(u'豆瓣实习', 'failed', date(2012,3,3), [u'产品开发实习生'], u'笔试面试都在卖萌...（羞', date(2012,3,26))
#create_one(u'腾讯实习', 'failed', date(2012,3,26), [u'后台开发实习生', u'游戏开发实习生'], u'人太搓，没救了 ╮(￣▽￣")╭', date(2012,4,23))
#create_one(u'网易游戏', 'failed', date(2012,3,30), [u'Web基础平台架构实习生'], u'投晚了几天……', date(2012,3,30))
#create_one(u'创新工场', 'posted', date(2012,3,12), [u'软件开发实习生'], u'就一个公司面试我，还没开始？', None)
#create_one(u'网易有道', 'posted', date(2012,3,30), [u'研发实习攻城师'], u'', None)
#create_one(u'百度实习', 'posted', date(2012,4,6), [u'百度音乐事业部-搜索实习研发攻城师'], u'', None)
