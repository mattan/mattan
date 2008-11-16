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
          
              
              
class MainPage2(webapp.RequestHandler):  
  def get(self):    
      self.response.out.write('<html><body>'                            
                              '<form method="POST" '                            
                              'action="/">'                            
                              '<table>')    
      # This generates our shopping list form and writes it in the response    
      self.response.out.write(ItemForm())    
      self.response.out.write('</table>'                            
                              '<input type="submit">'                            
                              '</form></body></html>')
  def post(self):    
      data = ItemForm(data=self.request.POST)    
      if data.is_valid():      
          # Save the data, and redirect to the view page      
          entity = data.save(commit=False)      
          entity.added_by = users.get_current_user()      
          entity.put()      
          self.redirect('/items.html')    
      else:      
          # Reprint the form      
          self.response.out.write('<html><body>'                              
                                  '<form method="POST" '                              
                                  'action="/">'                              
                                  '<table>')      
          self.response.out.write(data)     
          self.response.out.write('</table>'                              
                                  '<input type="submit">'                              
                                  '</form></body></html>')
              
 
#just a engin - ignor
from pprint import pprint
def issub(c,x):
    try:
        return issubclass(c, x)
    except TypeError:
        return False
    appline = filter(lambda x: issub(x[1], webapp.RequestHandler),vars().items() )
    appline = map(lambda x: ("/"+x[0],x[1]),appline)
    pprint(appline)



application = webapp.WSGIApplication(
                                           [('/', MainPage2),
                                           ('/sign', mattanapp),
                                           ('/sign2/', mattanapp2),
                                           ('/kipkip', kipaValidate),
                                           ('/historyPage', historyPage),
                                           
                                           #('/view-table-no-', kipaValidate),
                                           #^/view-(.*)-no-(.*)$
                                           #solve = re.compile("^/view-(.*)-no-(.*)$")
                                           #solve.findall(a)[0]
                                           #
                                           #warning! "^/view-([^-]*)-no-([^-]*)$"
                                           ('/view-([^-]*)-number-([^-]*)$', smartreq),
                                           ('/edit-([^-]*)-number-([^-]*)$', smartreq),
                                           ('/delete-([^-]*)-number-([^-]*)$', smartreq),
                                           ('/create-([^-]*)-number-([^-]*)$', smartreq),
                                           
                                           ('/view-([^-]*)()$', smartreq),
                                           ('/edit-([^-]*)()$', smartreq),
                                           ('/delete-([^-]*)()$', smartreq),
                                           ('/create-([^-]*)()$', smartreq),
                                           ('/choose-([^-]*)()$', smartreq),
                                           
                                           ('/nothing', historyPage)],
                                           debug=True)
  
def main():
    run_wsgi_app(application)
if __name__ == "__main__":
    main()     