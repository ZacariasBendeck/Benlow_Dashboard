from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User, Price_List, Mtd_Sales

engine = create_engine('sqlite:///Benlow.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


try:
    num_rows_deleted = session.query(Mtd_Sales).delete()
    session.commit()
except:
    print 'Price_list table was not cleared!!!'
    session.rollback()