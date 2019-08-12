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
from werkzeug.contrib.sessions import SessionMiddleware, FilesystemSessionStore
from werkzeug.contrib.securecookie import SecureCookie


session_store = FilesystemSessionStore()


class Shop(object):

    def __init__(self):
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)  
        self.url_map = Map([
            Rule('/', endpoint='index_url'),
            Rule('/search', endpoint='search_data'),
#            Rule('/add', endpoint='add_to_cart')
        ])
    
    def index_url(self, request):
        #import pdb;pdb.set_trace()
        data = self.csv_reader()
        cookie_data = request.cookies.get('cart_cookie')
        final_result = []
        if cookie_data:
            cookie = json.loads(cookie_data) #,product_detail=cookie_data
            print(cookie)
            #self.search()

            # found = {}
            # with open('Products/data.csv', 'r') as f_in:
            #     csv_reader = csv.reader(f_in, delimiter=',', quotechar='"')
            #     lines = [line for line in csv_reader if line]
            #     data = [dict(zip(lines[0], l)) for l in lines[1:]]
            #     found = [i for i in data if word in (i['product'].strip(),i['id'].strip())]

            #     for id, product , price in csv_reader:
            #         if found[0]['id'] in cookie:
            # #final_result.setdefault('id', []).append(product)
            #             # found.setdefault('product', []).append(product)
            #             # found.setdefault('price', []).append(price)
            #             return found
            ################################################################
            # found = self.search(request.args.get('search_string'))
            # response = Response(json.dumps(found), mimetype='application/json')

            with open('Products/data.csv', 'r') as f_in:
                reader = csv.reader(f_in)
                next(reader)
                for line in reader:
                    if line[0] in cookie:
            #final_result.setdefault('id', []).append(product)
                        final_result.append(line)
                #return response
            print(final_result)

        return self.render_template('index.html',data=data,cart_data=final_result)

    def search(self,word):
        found = []
        with open('Products/data.csv', 'r') as f_in:
            csv_reader = csv.reader(f_in, delimiter=',', quotechar='"')
            lines = [line for line in csv_reader if line]
            data = [dict(zip(lines[0], l)) for l in lines[1:]]
            found = [i for i in data if word in (i['product'].strip(),i['id'].strip())]
        return found


    #def check_out(self,word):


    def search_data(self, request):
        #found = []
        if request.method == "POST":
            # word = request.args.get('search_string')
            # with open('Products/data.csv', 'r') as f_in:
            #     csv_reader = csv.reader(f_in, delimiter=',', quotechar='"')
            #     lines = [line for line in csv_reader if line]
            #     data = [dict(zip(lines[0], l)) for l in lines[1:]]

            # # found = [i['id'] for i in data if word in (i['product'].strip(),i['id'].strip())]
            # found = [i for i in data if word in (i['product'].strip(),i['id'].strip())]
            found = self.search(request.args.get('search_string'))
            response = Response(json.dumps(found), mimetype='application/json')
            print(found)   

            #if request.args.get('add_to_cart'):
             #   response.set_cookie('cart_cookie',json.dumps(found))

            # if request.args.get('add_to_cart'):
            #     cookie_data = request.cookies.get('cart_cookie')
            #     print(cookie_data)
            #     response.set_cookie('cart_cookie',json.dumps(found))


            if request.args.get('add_to_cart'):
                cookie_data = request.cookies.get('cart_cookie')
                cookie = set()

                if cookie_data:
                    cookie = set(json.loads(cookie_data))  
                
                cookie.add(found[0]['id'])
                response.set_cookie('cart_cookie',json.dumps( list(cookie) ))

            return response   

    def csv_reader(self):
        rdr= csv.reader( open("Products/data.csv", "r" ) )
        header = next(rdr,None)
        csv_data = [ row for row in rdr ]

        # if not request.cookies.get('id_cookie'):
        #     response=Response("user is not valid")
        #     return response(environ, start_response)
        # else:
        #     return csv_data

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
        #response.set_cookie('id_cookie',number)
        return response(environ, start_response) 

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def __call__(self, environ, start_response):

        return self.wsgi_app(environ, start_response)

def create_app(with_static=True):
    app = Shop()
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)



