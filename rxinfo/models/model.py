from rxinfo import DB2
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Users(DB2.Model):
    # __tablename__ = 'tbl_users'
    # __table_args__ = { 'autoload': True, 'schema': 'data', 'autoload_with': db.engine }
    __table__ = DB2.Table('tbl_users', Base.metadata, autoload=True, autoload_with=DB2.engine)
    def __repr__(self):
        return '<User {}>'.format(self.full_name)