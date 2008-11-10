from smartreq import *

class mattanapp(webapp.RequestHandler):
    def get(self):
        if(users.get_current_user()):
            Name=users.get_current_user()
            Login=users.create_logout_url("/sign")
        else:
            self.redirect(users.create_login_url("/sign"))
            return
        

        a = db.Key.from_path("man",users.get_current_user().email())
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
