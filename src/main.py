import cgi
import urllib

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch

from historyPage import *
from database import *

class MainPage(webapp.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write('Hello, webapp World!')


class mattanapp(webapp.RequestHandler):
    def get(self):
        if(users.get_current_user()):
            Name=users.get_current_user()
            Login=users.create_logout_url("/sign")
        else:
            self.redirect(users.create_login_url("/sign"))
            return
        

        a = db.Key.from_path("man",users.get_current_user().email())      
        if (man.get(a)):
            Me = man.get(a)
        else:
            Me = man(key_name=users.get_current_user().email())
            
        
        greetings_query = friends1.all()
        greetings = greetings_query.fetch(9999)
        for g in greetings:
            g.delete()
        Login = users.create_logout_url("/sign")
        Name = users.get_current_user().email()
        
        #users.create_login_url("/sign")
        template_values = {
                          'Fs': man.all(),
                          'Login': Login,
                          'Name': Name,
                          'Me': Me
                          }
        path = os.path.join(os.path.dirname(__file__), 'friends.html')
        self.response.out.write(template.render(path , template_values))       
        #self.response.out.write(urlfetch.fetch("http://www.kipa.co.il/").content)
class mattanapp2(webapp.RequestHandler):
    def post(self):
        if(users.get_current_user()):
            Name=users.get_current_user()
            Login=users.create_logout_url("/sign")
        else:
            self.redirect(users.create_login_url("/sign"))
            return

        #Me = man(None,users.get_current_user().email())
        a = db.Key.from_path("man",users.get_current_user().email())      
        if (man.get(a)):
            Me = man.get(a)
        else:
            Me = man(key_name=users.get_current_user().email())
            
        Me.nickM=cgi.escape(self.request.get('content'))
        Me.ID=users.get_current_user()
        Me.put()
        
        self.redirect("/sign" )    
        #self.response.out.write(urlfetch.fetch("http://www.kipa.co.il/").content)

class kipaValidate(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'HTMLPage1.htm')
        self.response.out.write(template.render(path , {}))
 
class kipaValidate2(webapp.RequestHandler):
    def post(self):
        m = self.request
        self.response.out.write("result.status_code:")
        M=self.request.get('kipanick')
        self.response.out.write("<BR>")
        for arg in self.request.arguments():
            self.response.out.write(arg+"="+self.request.get(arg)+"<BR>")
        form_fields = {  "nick":M,  "password":self.request.get('kipapass') }
        form_data = urllib.urlencode(form_fields)
        result = urlfetch.fetch(url="http://www.kipa.co.il/my/login2.asp",
                                payload=form_data,
                                method=urlfetch.POST,
                                headers={'Content-Type': 'application/x-www-form-urlencoded ; charset=utf-8'})
        if (not "function check1()" in result.content):
            self.response.out.write("yep")
        else:
            self.response.out.write("nop")
        #self.get()
        #self.response.out.write(result.content)
        
###לפרק את הקוד לחלקים VX
###ללמוד על AJAX 
###למצוא דרך נוחה לעבוד עם הDB
### להתחבר לגוגל CODE
### לשנות את הצבע של ההערות
### getattr(obj,"meth") לחבר קוד לתיבת טקסט
### האם אני צריך לכתוב כל דבר 7 פעמים?
### איך עושים cgi.escape( בHTML

#just a engin - ignor 
application = webapp.WSGIApplication(
                                           [('/', MainPage),
                                           ('/sign', mattanapp),
                                           ('/sign2', mattanapp2),
                                           ('/kipkip', kipaValidate),
                                           ('/kipkip2', kipaValidate2),
                                           ('/historyPage', historyPage)],
                                           debug=True)
  
def main():
    run_wsgi_app(application)
if __name__ == "__main__":
    main()     