from rxinfo import DB
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Users(DB.Model):
    # __tablename__ = 'tbl_users'
    # __table_args__ = { 'autoload': True, 'schema': 'data', 'autoload_with': db.engine }
    __table__ = DB.Table('tbl_users', Base.metadata, autoload=True, autoload_with=DB.engine)
    def __repr__(self):
        return '<User {}>'.format(self.full_name)


class Patient(DB.Model):    
    __table__ = DB.Table('tbl_patients', Base.metadata, autoload=True, autoload_with=DB.engine)
    def __repr__(self):
        return '<Patient {}>'.format(self.id)