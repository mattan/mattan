from database import *
from google.appengine.ext.db import Key 
import django.template.loader 

class smartreq(webapp.RequestHandler):
    def updateHistory(self):
        record=history()
        record.data=""
        for arg in self.request.arguments():
            record.data+=arg+"="+self.request.get(arg)+"&"
        record.ip=self.request.remote_addr
        record.URL=self.request.url
        #self.response.out.write(record.__dict__)
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
    def showPage(self,action,table,Mkey):
        #to do test Mkey validation...
        try:
            #if (action=="view" or action=="edit" or action=="create"):
            if (not Mkey or Mkey==""): 
                x=db.class_for_kind(table).all()
                for a in x:
                    self.response.out.write(a.editS())
            else: 
                a=db.class_for_kind(table).get_or_insert(Mkey)
                a.keyInit()
                self.response.out.write(a)
            #filter a from problems
            #self.response.out.write(str(a.test2))
            #path = os.path.join(os.path.dirname(__file__), table+'Page1.html')
            #self.response.out.write(template.render(path , template_values))
            #django.template.loader.get_template_from_string(source, origin, name)
            #http://docs.djangoproject.com/en/dev/ref/templates/api/?from=olddocs
        except db.KindError:
            #to do something better
            self.response.out.write("what is "" " + table + " ""?!")

    def handlePage(self,action,table,Mkey):
        #to do test Mkey validation...
        #to do test Mkey !="" and !=^[0-9]  
        #to do consider to get Mkey from self.request.get("Mkey")  
        try:
            a=db.class_for_kind(table).get_or_insert(Mkey)
            #self.response.out.write(self.request.arguments())
            for arg in self.request.arguments():
                a.__setattr__(arg,self.request.get(arg))
            #filter a from problems
            a.put()
            #self.justatest(table,Mkey)
        except db.KindError:
            self.response.out.write("what is "" " + table + " ""?!")
            return
            
        
    def get(self,action,table,Mkey):
        self.validateUser() #includes save last login time
        self.updateHistory()
        self.showPage(action,table,Mkey)
    def post(self,action,table,Mkey):
        self.validateUser() #includes save last login time
        self.updateHistory()
        self.handlePage(action,table,Mkey)
        self.get(action,table,Mkey)
        
    
    
        