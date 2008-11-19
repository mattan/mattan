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
    def view(self):
        return objshow().view(self) 
    def editS(self):
        return objshow().edit(self,"S") 
    def viewS(self):
        return objshow().edit(self,"S") 
    #def Mdel(self):
    #    return objshow().Mdel(self) 
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
    URLkey = db.StringProperty(multiline=False)
    def keyInit(self):
        self.URLkey = "edit-" + str(self.key().kind()) + "-number-" + str(self.key().name())
   #validator=^[a-z]*$
        #[x for x in a if x in b]==[]
        
        
class man(securitydata): #never delete use to track how on line
    nickM = db.StringProperty(multiline=False)
    passM = db.StringProperty(multiline=False)
    ok = db.StringProperty(multiline=False, default="No") 
    def kipatest(self):
        form_fields = {  "nick":unicode(nickM),  "password":unicode(passM) }
        form_data = urllib.urlencode(form_fields)
        result = urlfetch.fetch(url="http://www.kipa.co.il/my/login2.asp",
                                payload=form_data,
                                method=urlfetch.POST,
                                headers={'Content-Type': 'application/x-www-form-urlencoded ; charset=utf-8'})
        if (not "function check1()" in result.content):
            i=i
        else:
            ok="YES!"
            group.get_or_insert(users.get_current_user().email()+"%kip%",Title="%kip%").save()
        group.get_or_insert(users.get_current_user().email()+"%all%",Title="%%all%%").save()
            

class group(securitydata):
    "the items that let you enter to pages"
class HTML(securitydata):
    ThePage = db.TextProperty()
    "the pages"
class profile(securitydata):
    "the profile of each user"
    def keyInit(self):
        securitydata.keyInit(self)
        self.Sedit = self.key().name()

class sendBox1(securitydata):
    "nothing special"
class sendBox2(securitydata):
    "nothing special"
class sendBox3(securitydata):
    "nothing special"
class sendBox4(securitydata):
    "nothing special"
class sendBox5(securitydata):
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
    def valid(self,r):
        if not re.search("^[a-z]*$",str(r)):
            raise "wrong"
        
    def error(self,itemT,param=""):
        template_values = Context(itemT._entity) 
        page=HTML.get_or_insert("error"+param+"."+str(itemT.key().kind()))
        template=Template(str(page.ThePage))      
        return(template.render(template_values))        
    def view(self,itemT,param=""):
        if not self.securityTest(itemT.Sview.split(","),itemT.ID):
            return self.error(itemT,param)
        #itemT._entity["URLkey"]=self.keyTest(itemT)
        template_values = Context(itemT._entity) 
        page=HTML.get_or_insert("view"+param+"."+str(itemT.key().kind()))
        template=Template(str(page.ThePage))      
        return(template.render(template_values))        
    def edit(self,itemT,param=""):
        if not self.securityTest(itemT.Sedit.split(","),itemT.ID):
            return self.view(itemT,param)
        template_values = Context(itemT._entity) 
        page=HTML.get_or_insert("edit"+param+"."+str(itemT.key().kind()))
        if not page.ThePage:
            page.ThePage="""
<head>
<title>Mattan</title>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
</head>
<body dir="ltr">
<form method="POST">
<input type="submit" value="submit">
<textarea id="Text1" cols="50" rows="25" name="ThePage"/>{{ ThePage|escape }}</textarea>
</form>
{{ ThePage|escape }}
</body>
</html>
 """
        template=Template(str(page.ThePage))      
        return(template.render(template_values))
        #path = os.path.join(os.path.dirname(__file__), 'HTMLPage1.html')
        #django.template.loader.get_template_from_string(source, origin, name)
        #http://docs.djangoproject.com/en/dev/ref/templates/api/?from=olddocs