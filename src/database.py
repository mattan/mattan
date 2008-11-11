from import_tools import *

from google.appengine.ext import db

class Item(db.Expando):  
    name = db.StringProperty()  
    quantity = db.IntegerProperty(default=1)  
    target_price = db.FloatProperty()  
    priority = db.StringProperty(default='Medium',choices=[    'High', 'Medium', 'Low'])  
    entry_time = db.DateTimeProperty(auto_now_add=True)  
    added_by = db.UserProperty()


class userdata(db.Expando):
    ID = db.UserProperty() #the data creator
    date = db.DateTimeProperty(auto_now_add=True)
    cdate = db.DateTimeProperty(auto_now=True)
    def __init__(self,*args, **kw):
        db.Model.__init__(self,*args,**kw)
        self.ID = users.get_current_user()
        #return self
    def to_html(self):
        return('<a href="' +
                "byby" + '">' +
                str(self.ID.email()) + "btbtb" +
                "</a><BR>")
        
class securitydata(userdata):
    Mread = db.StringListProperty()
    MWrite = db.StringListProperty()
    Title = db.StringProperty(multiline=False)
    URLkey = db.StringProperty(multiline=False)#validator=^[a-z]*$
    
class group(securitydata):
    "nothing special"
class HTML(securitydata):
    "nothing special"    

 

    
class man(userdata): #never delete use to track how on line
    nickM = db.StringProperty(multiline=True)
    passM = db.StringProperty(multiline=False)
    def __str__(self):
        if (self.nickM):
            return self.nickM
        return "<BR>i<BR>"

       
class kind(userdata):
    description = db.StringProperty(multiline=False)
 

class friends1(userdata):
    fromF = man
    toF = man
    value = kind
    notes = db.StringProperty(multiline=True)
      
class history(userdata):#never delete use to track what happening
    ip = db.StringProperty(multiline=False) #remote_addr
    URL = db.StringProperty(multiline=False)
    data = db.StringProperty(multiline=False)
    test2 = db.SelfReferenceProperty()


class ItemForm(djangoforms.ModelForm):  
    class Meta:    
        model = history    
        exclude = ['added_by']