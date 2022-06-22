import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
'''
setup_db(app):
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    database_name ='local_db_name'
    default_database_path= "postgres://{}:{}@{}/{}".format('postgres', 'password',
'localhost:5432', database_name)
    database_path = os.getenv('DATABASE_URL', default_database_path)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
'''
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class Url(db.Model):

    __tablename__ = 'urlvalues'
    id = Column(Integer, primary_key=True)
    url = Column(String(2048))
    company = Column(String, default = "company not added yet")
    description = Column(String, default = "description not added yet")

    def __init__(self, url, company, description):
        self.url = url
        self.company = company
        self.description = description

    def details(self):
        return {
            'id': self.id,
            'url': self.url,
            'company': self.company,
            'description': self.description
        }
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
