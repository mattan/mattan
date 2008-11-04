from smartreq import *

class historyPage(smartreq):
    def showPage(self):
        template_values = {'Table': history.all()}
        path = os.path.join(os.path.dirname(__file__), 'historyPage.html')
        self.response.out.write(template.render(path , template_values))