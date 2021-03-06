""" basic tody list using webpy """
import web
import model

urls= (
    '/','index',
    '/del/(\d+)','delete'
)
render=web.template.render('templates',base='base')

class index:
    form = web.form.Form(
        web.form.Textbox('title',web.form.notnull,
                         description="i need to:"),
        web.form.Button('add todo'),
        )
    def GET(self):
        """ show page """
        todos = model.get_todos()
        form = self.form()
        return render.index(todos,form)

    def POST(self):
        """ add new entry """
        form = self.form()
        if not form.validates():
            todos = model.get_todos()
            return render.index(todos,form)
        model.new_todo(form.d.title)
        raise web.seeother('/')

class delete:
    def POST(self,id):
        """ delete based on id """
        id=int(id)
        model.del_todo(id)
        raise web.seeother('/')

app=web.application(urls,globals())

if __name__=="__main__":
    app.run()
