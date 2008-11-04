from smartreq import *


class kipaValidate(smartreq):
    #def __init__(html_name):
    #    self.html_name=html_name
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'HTMLPage1.htm')
        self.response.out.write(template.render(path , {}))
    def post(self):
        form_fields = {  "nick":unicode(self.request.get('kipanick')),  "password":unicode(self.request.get('kipapass')) }
        form_data = urllib.urlencode(form_fields)
        result = urlfetch.fetch(url="http://www.kipa.co.il/my/login2.asp",
                                payload=form_data,
                                method=urlfetch.POST,
                                headers={'Content-Type': 'application/x-www-form-urlencoded ; charset=utf-8'})
        if (not "function check1()" in result.content):
            self.response.out.write("yep")
        else:
            self.response.out.write("nop")
        self.get()
        #self.response.out.write(result.content)