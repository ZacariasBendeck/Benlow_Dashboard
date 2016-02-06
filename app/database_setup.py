import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

### CLASS Code ###
class  User(Base):
    ### TABLE INFORMATION ###
    __tablename__ = 'users'

    ### MAPPERS ###
    name = Column(String(80), nullable = False)
    description = Column(String(250))
    pic_url = Column(String(1000))
    slogan = Column(String(250))
    created = Column(String(100))
    updated = Column(String(100))
    email = Column(String(250), nullable = False)
    id =  Column(Integer, primary_key = True)

    @property
    def serialize(self):
        return {
        'name' : self.name,
        'description' : self.description,
        'pic_url': self.pic_url,
        'id': self.id,
        "created" : self.created,
        "updated" : self.updated,
        'slogan' : self.slogan,
        'email' : self.email
        }


########insert at the end of the file  ###############
#####
engine = create_engine('sqlite:///dashboardBenlow.db')

Base.metadata.create_all(engine)