# This Python file uses the following encoding: utf-8

#from import_tools import *

from historyPage import *

from smartreq import *
from kipaValidate import *
from mattanapp import *

class MainPage(webapp.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write('Hello, webapp World!')
              
 
#just a engin - ignor
def issub(c,x):
    try:
        return issubclass(c, x)
    except TypeError:
        return False
appline = filter(lambda x: issub(x[1], webapp.RequestHandler),vars().items() )
appline = map(lambda x: ("/"+x[0],x[1]),appline)
from pprint import pprint

pprint(appline)
application = webapp.WSGIApplication(
                                           [('/', MainPage),
                                           ('/sign', mattanapp),
                                           ('/sign2/', mattanapp2),
                                           ('/kipkip', kipaValidate),
                                           ('/historyPage', historyPage)],
                                           debug=True)
  
def main():
    run_wsgi_app(application)
if __name__ == "__main__":
    main()     