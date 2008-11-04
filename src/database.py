from google.appengine.ext import db
from google.appengine.api import users

class userdata(db.Model):
    ID = db.UserProperty() #the data creator
    date = db.DateTimeProperty(auto_now_add=True)
    cdate = db.DateTimeProperty(auto_now=True)
    def __init__(self,*args, **kw):
        db.Model.__init__(self,*args,**kw)
        self.ID = users.get_current_user()
        #return self

    
class man(userdata):
    nickM = db.StringProperty(multiline=True)
    passM = db.StringProperty(multiline=False)

       
class kind(userdata):
    description = db.StringProperty(multiline=False)
 

class friends1(userdata):
    fromF = man
    toF = man
    value = kind
    notes = db.StringProperty(multiline=True)
      
class history(userdata):
    ip = db.StringProperty(multiline=False) #remote_addr
    URL = db.StringProperty(multiline=False)
    data = db.StringProperty(multiline=False)
