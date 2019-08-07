import os
#import redis
#import urlparse
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader
import jinja2
import csv
import json

class Shop(object):

    def __init__(self):
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)  
        self.url_map = Map([
            Rule('/', endpoint='index_url'),
            Rule('/search', endpoint='search_data'),
            Rule('/add', endpoint='add_to_cart')
        ])
    
    def index_url(self, request):
        #import pdb;pdb.set_trace()
        data = self.csv_reader()
        return self.render_template('index.html',data=data)

    def search_data(self, request):
        found = []
        if request.method == "POST":
            word = request.args.get('search_string')
            with open('Products/data.csv', 'r') as f_in:
                csv_reader = csv.reader(f_in, delimiter=',', quotechar='"')
                lines = [line for line in csv_reader if line]
                data = [dict(zip(lines[0], l)) for l in lines[1:]]

            found = [i for i in data if word in i['product'].strip()]

        return Response(json.dumps(found), mimetype='application/json')     

    def add_to_cart(self, request):
        data = self.csv_reader()
        return self.render_template('index.html',data=data)

    def csv_reader(self):
        rdr= csv.reader( open("Products/data.csv", "r" ) )
        header = next(rdr,None)
        csv_data = [ row for row in rdr ]
        return csv_data

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, endpoint)(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)

        return response(environ, start_response) 

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def __call__(self, environ, start_response):

        return self.wsgi_app(environ, start_response)

def create_app():
    app = Shop()

    return app

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)



