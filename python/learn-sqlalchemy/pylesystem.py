import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from pyinotify import *

path = "/tmp"

engine = create_engine('sqlite:///meta.db',echo=True)
Base = declarative_base()

Session = scoped_session(sessionmaker(bind=engine))

class Filesystem(Base):
    __tablename__ = 'Filesystem'

    path = Column(String,primary_key=True)
    name = Column(String)

    def __init__(self,path,name):
        self.path = path
        self.name = name

    def __repr__(self):
        return "<MetaData('%s','%s')>" %(self.path,self.name)

def transactional(fn):
    """add transactional semantics to a method."""

    def transact(self,*args):
        session = Session()
        try:
            fn(self,session,*args)
            session.commit()
        except:
            session.rollback()
            raise
    transact.__name__ = fn.__name__
    return transact

class ProcessDir(ProcessEvent):
    """ Performs Actions based on mask values"""

    @transactional
    def process_IN_CREATE(self,session,event):
        print "Creating file and file record:",event.pathname
        create_record = Filesystem(event.pathname,event.path)
        session.add(create_record)

    @transactional
    def process_IN_DELETE(self,session,event):
        print "Removing:",event.pathname
        delete_record = session.query(Filesystem).filter_by(path=event.pathname).one()

        session.delete(delete_record)


def init_repository():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()

    for dirpath,dirnames,filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath,file)
            record = Filesystem(fullpath,file)
            session.add(record)
        session.flush()

    for record in session.query(Filesystem):
        print "Database Record Number: Path:%s,File:%s" %(record.path,record.name)

    session.commit()

if __name__ == '__main__':
        init_repository()
        wm = WatchManager()
        mask = IN_DELETE|IN_CREATE
        notifier = ThreadedNotifier(wm,ProcessDir())
        notifier.start()
        wdd = wm.add_watch(path,mask,rec = True)

