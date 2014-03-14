from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey

Base = declarative_base()

class Filesystem(Base):
    __tablename__ = 'filesystem'

    path = Column(String,primary_key=True)
    name = Column(String)

    def __init__(self,path,name):
        self.path = path
        self.name = name

    def __repr__(self):
        return "<Metadata(%s,%s)>" %(self.path,self.name)
