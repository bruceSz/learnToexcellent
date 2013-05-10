import web 
render  = web.application.render('templates/',cache=False)
urls = ('/(.*)','index')
app.web.application(urls,globals())
class index:
    def GET(self,code):
        web.header('Content-Type','text/xml')
        return render.response(code)

web.webapi.internalerror = web.debugerr
if __name__ =="__main__":app.run()
