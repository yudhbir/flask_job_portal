from rxinfo import db
from rxinfo import db.PrimaryKeyConstraint

class User(db.Model):
    __tablename__ = "users"
    __table_args__ = (
        PrimaryKeyConstraint('id'),
    )

    def __init__(self, name):
        self.name = name