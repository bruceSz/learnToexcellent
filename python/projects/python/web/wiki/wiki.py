""" basic wiki using webpy """

import web
import model
import markdown
###url mappings
urls=(
    '/','index',
    '/new','new',
    '/edit/(\d+)','edit',
    '/delete/(\d+)','delete',
    '/(.*)','page',
)

t_globals={
    'datestr':web.datestr,
    'markdown':markdown.markdown,
}

render = web.template.render('templates',base='base',globals=t_globals)

class index:
    def GET(self):
        ''' show page'''
        pages = model.get_pages()
        return render.index(pages)

class page:
    def GET(self,url):
        ''' view single page'''
        page = model.get_page_by_url(url)
        if not page:
            raise web.seeother('/new?url=%s' %web.websafe(url))
        return render.view(page)


class new:
    def not_page_exists(url):
        return not bool(model.get_page_by_url(url))
    
    page_exists_validator = web.form.Validator('page already exists',
                                               not_page_exists)

    form = web.form.Form(
        web.form.Textbox('url',web.form.notnull,page_exists_validator,
                         size=30,
                         description="location:"),
        web.form.Textbox('title',web.form.notnull,
                         size=30,
                         description="page title:"),
        web.form.Textarea('content',web.form.notnull,
                          rows=30,cols=80,
                          description="page content:",post="use markdown syntax"),
        web.form.Button('create page'),
     )

    def GET(self):
        url=web.input(url='').url
        form=self.form()
        form.fill({'url':url})
        return render.new(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_page(form.d.url,form.d.title,form.d.content)
        raise web.seeother('/'+form.d.url)


class delete:
    def POST(self,id):
        model.del_page(int(id))
        raise web.seeother('/')

class edit:
    form = web.form.Form(
        web.form.Textbox('url',web.form.notnull,
                         size=30,
                         description="location:"),
        web.form.Textbox('title',web.form.notnull,
                         size=30,
                         description="page title:"),
        web.form.Textarea('content',web.form.notnull,
                          rows=30,cols=80,
                          description="page content",post="use markdown syntax"),
        web.form.Button('update page'),
    )

    def GET(self,id):
        page=model.get_page_by_id(int(id))
        form = self.form()
        form.fill(page)
        return render.edit(page,form)

    def POST(self,id):
        form = self.form()
        page = model.get_page_by_id(int(id))
        if not form.validates():
            return render.edit(page,form)
        model.update_page(int(id),form.d.url,form.d.title,form.d.content)
        raise web.seeother('/')

app =web.application(urls,globals())
if __name__=="__main__":
    app.run()
