import os
from google.appengine.ext import webapp
from database import *
from google.appengine.ext.webapp import template
from google.appengine.api import users

class smartreq(webapp.RequestHandler):
    def updateHistory(self):
        record=history().init()
        for arg in self.request.arguments():
            record.data+=arg+"="+self.request.get(arg)+"&"
        record.ip=self.request.remote_addr
        record.URL=self.request.url
        record.put()
    def validateUser(self): #Logout=users.create_logout_url("/sign")
        if(not users.get_current_user()):
            self.redirect(users.create_login_url(self.request.url))
        if(users.get_current_user()):
            me=man.get_or_insert(users.get_current_user().email())
            me.put()#just to change the time...
            self.response.out.write('<a href="' +
                users.create_logout_url(self.request.url) + '">' +
                str(me.nickM) +
                "</a><BR>") 
    
    def get(self):
        self.validateUser() #includes save last login time
        self.updateHistory()
        self.showPage()
    def post(self):
        self.validateUser() #includes save last login time
        self.updateHistory()
        self.handlePage()
        self.get()
    
        