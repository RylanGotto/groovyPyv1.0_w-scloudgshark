
from tornado.web import RequestHandler
from routes import route

@route('/site')
class IndexHandler(RequestHandler):
    def get(self):
        #template context variables go in here
       	template_values = {}
        self.write("Hello World!")
