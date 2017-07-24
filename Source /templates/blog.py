import cgi
import wsgiref.handlers
from google.appengine.api import users
import webapp2
 
MAIN_HTML = open('main.html').read()
NEW_HTML = open('new.html').read()
dic = {}

class MainPage(webapp2.RequestHandler):
    def get(self):

        self.response.write(MAIN_HTML)
               
    def post(self):
        self.response.write(MAIN_HTML)
        self.response.out.write('<html><body>')
        for key in dic:
            self.response.out.write('<br>Title: <pre>')
            self.response.out.write(key)
            self.response.out.write('<br></pre>Content: <pre>')
            self.response.out.write(dic[key])
            self.response.out.write('<br>')
        self.response.out.write('<br></pre>')
        self.response.out.write('<br></pre></body></html>')
        
           
class NewPage(webapp2.RequestHandler):
    def get(self):
        
        self.response.write(NEW_HTML)
        
class BlogItPage(webapp2.RequestHandler):
    def post(self):
        self.response.out.write("""<html><head><title>Blogged It Page</title>
                                <link href="stylesheets/blogitstyle.css" rel="stylesheet" type="text/css" >
                                </head>
                                <body>Title: <pre>""")
        self.response.out.write(cgi.escape(self.request.get('title')))
        self.response.out.write('</pre>Content: <pre>')
        self.response.out.write(cgi.escape(self.request.get('content')))
        self.response.out.write("""</pre><form action="/mainpage" method="post">
                                <br><div>
                                <input type="submit" value="Back to Main Page">
                                </div></form>""")
        self.response.out.write('</body></html>')
        a = self.request.get('title')
        b = self.request.get('content')
        dic[a]=b
        
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/new.html', NewPage), 
    ('/sign', BlogItPage), 
    ('/mainpage', MainPage)
], debug=True)

def main():
    app.run()

if __name__ == "__main__":
    main()