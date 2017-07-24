import cgi

from google.appengine.api import users
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/sign" method="post">
                <div><textarea name="content" rows="3" cols="60"></textarea></div>
                <div><input type="submit" value="Sign Guestbook"></div>
              </form>
            </body>
          </html>""")

class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.out.write('<html><body>You wrote:<pre>')
        self.response.out.write(cgi.escape(self.request.get('content')))
        self.response.out.write('</pre></body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook)
], debug=True)

def main():
    application.run()

if __name__ == "__main__":
    main()
    
(r'/static/blog.css', CSSHandler),

class CSSHandler(webapp2.RequestHandler):
    def get(self, *args, **kwargs):
        with open('/home/eclipse-workspace/BlogProject/static/mainstyle.css') as f:
            response = webapp2.Response(f.read())
            response.content_type = 'text/css'
            return response


app = webapp2.WSGIApplication([
    ('/', MainPage),(r'/static/mainstyle.css', CSSHandler),
    ('/new.html', NewPage), 
    ('/sign', BlogItPage), 
    ('/mainpage', MainPage)
], debug=True)
