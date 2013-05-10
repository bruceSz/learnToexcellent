import web
db = web.database(dbn='mysql',db="test",user='zs',pw='123456')
def get_pages():
    return db.select('pages',order='id DESC')

def get_page_by_url(url):
    try:
        return db.select('pages',where="url=$url",vars=locals())[0]
    except IndexError:
        return None

def get_page_by_id(id):
    try:
        return db.select('pages',where='id=$id',vars=locals())[0]
    except IndexError:
        return None

def new_page(url,title,text):
    db.insert('pages',url=url,title=title,content=text)

def update_page(id,url,title,text):
    db.update('pages',where="id=$id",vars=locals(),
              url=url,title=title,content=text)


