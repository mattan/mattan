from database import *
from google.appengine.ext.db import Key 

class smartreq(webapp.RequestHandler):
    def updateHistory(self):
        record=history()
        record.data=""
        for arg in self.request.arguments():
            record.data+=arg+"="+self.request.get(arg)+"&"
        record.ip=self.request.remote_addr
        record.URL=self.request.url
        self.response.out.write(record.__dict__)
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
    def showPage(self,table,Mkey):
        #to do test Mkey validation...
        try:
            a=db.class_for_kind(table).get_or_insert(Mkey)
            #filter a from problems
            template_values = a._entity
            self.response.out.write(str(a._entity))
            path = os.path.join(os.path.dirname(__file__), table+'page1.html')
            self.response.out.write(template.render(path , template_values))
        except db.KindError:
            #to do something better
            self.response.out.write("what is "" " + table + " ""?!")

    def handlePage(self,table,Mkey):
        #to do test Mkey validation...
        #to do test Mkey !="" and !=^[0-9]  
        #to do consider to get Mkey from self.request.get("Mkey")  
        try:
            a=db.class_for_kind(table).get_or_insert(Mkey)
            for arg in self.request.arguments():
                a.__setattr__(arg,self.request.get(arg))
            #filter a from problems
            a.put()
        except db.KindError:
            #to do something better
            self.response.out.write("what is "" " + table + " ""?!")
            
        
    def get(self,table,Mkey):
        self.validateUser() #includes save last login time
        self.updateHistory()
        self.showPage(table,Mkey)
    def post(self,table,Mkey):
        self.validateUser() #includes save last login time
        self.updateHistory()
        self.handlePage(table,Mkey)
        self.get(table,Mkey)
    
        