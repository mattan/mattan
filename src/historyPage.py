import os
from google.appengine.ext import webapp
from database import *
from google.appengine.ext.webapp import template
from google.appengine.api import users
import datetime

from smartreq import *


class historyPage(smartreq):
    def showPage(self):
        template_values = {'Table': history.all()}
        path = os.path.join(os.path.dirname(__file__), 'historyPage.html')
        self.response.out.write(template.render(path , template_values))