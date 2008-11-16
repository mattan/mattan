from import_tools import *

from google.appengine.ext import db

class userdata(db.Expando):
    ID = db.UserProperty() #the data creator
    date = db.DateTimeProperty(auto_now_add=True)
    cdate = db.DateTimeProperty(auto_now=True)
    def __init__(self,*args, **kw):
        db.Model.__init__(self,*args,**kw)
        self.ID = users.get_current_user()
        #return self
    def __str__(self):
        return objshow().edit(self) 
    def to_html(self):
        return('<a href="' +
                "byby" + '">' +
                #str(self.ID.email()) + "btbtb" +
                "</a><BR>")
    
        
class securitydata(userdata):
    Sedit = db.StringProperty(multiline=False,default="%me%")
    Sview = db.StringProperty(multiline=False,default="%all%")
    Sdelete = db.StringProperty(multiline=False,default="%mng%")
    Title = db.StringProperty(multiline=False)
    URLkey = db.StringProperty(multiline=False)#validator=^[a-z]*$
        #[x for x in a if x in b]==[]

class group(securitydata):
    "nothing special"
class HTML(securitydata):
    ThePage = db.TextProperty()
    "nothing special"   

class objshow():
    def securityTest(self,Slist,isMe):
        if "%me%" in Slist:
            if isMe==users.get_current_user():
                return True
        for item in group.all().filter("ID=", users.get_current_user()):
            if item.Title in Slist:
                return True
        return False        
    def keyTest(self,itemT):
        return "edit-" + str(itemT.key().kind()) + "-number-" + str(itemT.key().name())
    def valid(self,r):
        if not re.search("^[a-z]*$",str(r)):
            raise "wrong"
        
    def edit(self,itemT):
        if not self.securityTest(itemT.Sedit.split(","),itemT.ID):
            return view(self,itemT)
        itemT._entity["URLkey"]=self.keyTest(itemT)
        template_values = Context(itemT._entity) 
        page=HTML.get_or_insert("edit"+"&"+str(itemT.key().kind()))     
        template=Template(page.ThePage)        
        return(template.render(template_values))
        #path = os.path.join(os.path.dirname(__file__), 'HTMLPage1.html')
        #django.template.loader.get_template_from_string(source, origin, name)
        #http://docs.djangoproject.com/en/dev/ref/templates/api/?from=olddocs