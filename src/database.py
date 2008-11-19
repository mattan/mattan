from objshow import *

from google.appengine.ext import db

class Item(db.Expando):  
    name = db.StringProperty()  
    quantity = db.IntegerProperty(default=1)  
    target_price = db.FloatProperty()  
    priority = db.StringProperty(default='Medium',choices=[    'High', 'Medium', 'Low'])  
    entry_time = db.DateTimeProperty(auto_now_add=True)  
    added_by = db.UserProperty()


    


       
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
    data = db.TextProperty()
    test2 = db.SelfReferenceProperty()


class ItemForm(djangoforms.ModelForm):  
    class Meta:    
        model = history    
        exclude = ['added_by']