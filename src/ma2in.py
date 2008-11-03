import cgi

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp.util import run_wsgi_app

class man(db.Model):
    ID = db.UserProperty()
    nickM = db.StringProperty(multiline=False)
    passM = db.StringProperty(multiline=False)
    date = db.DateTimeProperty(auto_now_add=True)
    
class kind(db.Model):
    ID = db.UserProperty()
    description = db.StringProperty(multiline=False)
    date = db.DateTimeProperty(auto_now_add=True)
 

class friends1(db.Model):
  fromF = man
  toF = man
  value = kind
  notes = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)

class webapp(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))






# junk!!!!!!


class Greeting(db.Model):
  author = db.UserProperty()
  content = db.StringProperty(multiline=True)
  to99 = db.StringProperty(multiline=False)
  date = db.DateTimeProperty(auto_now_add=True)

class Guestbook(webapp.RequestHandler):
  def post(self):
    greeting = Greeting()

    if users.get_current_user():
      greeting.author = users.get_current_user()

    greeting.content = self.request.get('content')
    greeting.put()
    self.redirect('/')

class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.out.write('<html><body>')

    greetings = Greeting.all()
    greetings.order("-date")
    # greetings.filter("author =", users.get_current_user())
    self.response.out.write("author ="+ str(users.get_current_user()))
    
    for greeting in greetings:
      if greeting.author:
        self.response.out.write('<b>%s</b> wrote:' % greeting.author.nickname())
      else:
        self.response.out.write('An anonymous person wrote:')
      self.response.out.write('<blockquote>%s</blockquote>' %
                              cgi.escape(greeting.content))
      self.response.out.write("##"+str(greeting.to99))

    # Write the submission form and the footer of the page
    self.response.out.write("""
          <form action="/sign" method="post">
            <div><textarea name="content" rows="3" cols="60"></textarea></div>
            <div><input type="submit" value="Sign Guestbook"></div>
          </form>
        </body>
      </html>""")
    
class TemplatePage(webapp.RequestHandler):
  def get(self):
    greetings_query = Greeting.all().order('-date')
    greetings = greetings_query.fetch(10)

    if users.get_current_user():
      url = users.create_logout_url(self.request.uri)
      u = users.get_current_user()
      url_linktext = ' '.join((u.email(),u.nickname(),u.auth_domain()))+' Logout'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'Login'

    template_values = {
      'greetings': greetings,
      'url': url,
      'url_linktext': url_linktext,
      }
    url99 = "http://www.zkoss.org/zkdemo/userguide/"
    url9 = "http://code.google.com/appengine/docs/gettingstarted/usingusers.html"
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))


class Guestbook(webapp.RequestHandler):
  def post(self):
    self.response.out.write('<html><body>You wrote:<pre>')
    self.response.out.write(cgi.escape(self.request.get('content')))
    self.response.out.write('</pre></body></html>')
    g = Greeting()
    g.content = self.request.get('content')
    g.to99 = "mattan"
    g.put()

application = webapp.WSGIApplication(
                                     [('/', webapp),
                                      ('/[a-z]', TemplatePage),
                                      ('/sign', Guestbook)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()