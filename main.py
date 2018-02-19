import tornado.ioloop
import tornado.web
import tornado.httpserver
import os.path


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", dynamic="Tornado")

    def post(self):
        self.render("index.html", dynamic="Tornado")


class Route1(tornado.web.RequestHandler):
    def get(self):
        self.write("This is good for the router exercice")


class Route2(tornado.web.RequestHandler):
    def get(self):
        self.render("page2.html")


class Route3(tornado.web.RequestHandler):
    def get(self):
        self.render("page3.html")


class RouteArgument(tornado.web.RequestHandler):
    def get(self):
        greet = self.get_argument('greet', 'Hello')
        self.write(greet + 'friendly user')


class Route4(tornado.web.RequestHandler):
    def get(self):
        self.render("page4.html", header_text="this is a templating text")


"""
UI MODULE
"""


class HelloModule(tornado.web.UIModule):
    def render(self):
        return '<p>This a module text</p>'

    def embedded_css(self):
        return " p {color: red}"


"""
FIN DU UI MODULE
"""


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler), (r"/page1", Route1), (r"/page2", Route2), (r"/", Route1), (r"/greet", RouteArgument), (r"/page3", Route3), (r"/page4", Route4)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"), ui_modules={"Hello": HelloModule}, debug=True
    )


if __name__ == "__main__":
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
