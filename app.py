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
#from werkzeug.contrib.sessions import SessionMiddleware, FilesystemSessionStore
#from werkzeug.contrib.securecookie import SecureCookie

# Creating E-Commerce Shoping Cart

class Shop(object):

# Main method 
    def __init__(self):

        # Joining Template Path
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)  
        # Making Controller 
        self.url_map = Map([
            Rule('/', endpoint='index_url'),
            Rule('/search', endpoint='search_data'),
            Rule('/check', endpoint='check_out')
        ])
# Function for rendering "index".
    def index_url(self, request):
        #import pdb;pdb.set_trace()

        # Read Data From CSV file
        data = self.csv_reader()
        # Get Cookie 
        cookie_data = request.cookies.get('cart_cookie')
        final_result = []
        if cookie_data:
            # Read Cookie Data
            cookie = json.loads(cookie_data) #,product_detail=cookie_data
            print(cookie)
            
            with open('Products/data.csv', 'r') as f_in:
                reader = csv.reader(f_in)
                next(reader)
                # Logic behind Refreshing of Page and See Updated Page
                for line in reader:
                    if line[0] in cookie:
                        final_result.append(line)
            print(final_result)

        return self.render_template('index.html',data=data,cart_data=final_result)
# Funtion for Search Item orr Value from Search Box
    def search(self,word):

        # Logic behind Searching Item or Value from Search Box
        found = []
        with open('Products/data.csv', 'r') as f_in:
            csv_reader = csv.reader(f_in, delimiter=',', quotechar='"')
            lines = [line for line in csv_reader if line]
            data = [dict(zip(lines[0], l)) for l in lines[1:]]
            found = [i for i in data if word in (i['product'].strip(),i['id'].strip())]
        return found

# Function for Check-Out Button

    def check_out(self, request):

        if request.method == "POST":
                        
            response = Response(mimetype='text/csv')
            # Get Cookie Data
            cookie_data = request.cookies.get('cart_cookie')
            final_result = []
            if cookie_data:
                # Read Cookie Data
                cookie = json.loads(cookie_data) 
                print(cookie)
                # Logic behind Saving Cart Data into CSV
                with open('Products/data.csv', 'r') as f_in:
                    reader = csv.reader(f_in)
                    next(reader)
                    for line in reader:
                        if line[0] in cookie:
                            final_result.append(line)
                            
                            with open("Products/cart_product.csv", "a", newline="") as f:
                                writer = csv.writer(f)
                                writer.writerows(final_result)
        return response            

# Function of Search Data which stores the cookie
    def search_data(self, request):
        if request.method == "POST":

            # While clicking on "Add To Cart" Button from these two line who are saving response in "list of dictionary" form.
            found = self.search(request.args.get('search_string'))
            response = Response(json.dumps(found), mimetype='application/json')
            print(found)   

            # Get Cookie Data
            if request.args.get('add_to_cart'):
                cookie_data = request.cookies.get('cart_cookie')
                cookie = set()
                # Read cookie Data
                if cookie_data:
                    cookie = set(json.loads(cookie_data))  
                
                # Only add "id" of cookie and get response of those ids in list format
                cookie.add(found[0]['id'])
                response.set_cookie('cart_cookie',json.dumps( list(cookie) ))

            return response   

# Function for reading CSV data 
    def csv_reader(self):
        rdr= csv.reader( open("Products/data.csv", "r" ) )
        # Removing Header
        header = next(rdr,None)
        csv_data = [ row for row in rdr ]

        return csv_data
# Function for Request
    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, endpoint)(request, **values)
        except HTTPException as e:
            return e
# Function of Request  Response of App
    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)

        return response(environ, start_response) 
# Function for Template Rendering
    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')
# Function for calling App
    def __call__(self, environ, start_response):

        return self.wsgi_app(environ, start_response)
# Function for Creating App
def create_app(with_static=True):
    app = Shop()
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app
# Main Method
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)



