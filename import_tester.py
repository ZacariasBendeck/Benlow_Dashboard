import json
import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

from app.models import Base, User, Price_List, Mtd_Sales


import time
from datetime import datetime
from pprint import pprint


engine = create_engine('sqlite:///Benlow.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

wkdir = os.getcwd()

# zapato_marca_hombre = session.query(Mtd_Sales).filter(Mtd_Sales.category.between(121,139))

# for i in zapato_marca_hombre:
#     print i.category_description
#     print i.price_list

# sum_by_sector = session.query(func.sum(Mtd_Sales.sector.label('total mtd qty')))
# for i in sum_by_sector.all():
#     print i


# zapatosdama = session.query(Mtd_Sales).filter(Mtd_Sales.category.between(566,600))
# zapatosdama2 = session.query(Mtd_Sales).filter(Mtd_Sales.category==566)

# items_seasonV = session.query(Price_List).filter_by(vendor='FORD').all()

# item = session.query(Mtd_Sales).filter(Mtd_Sales.sku=='0026BKD n')

# for i in item:
#     print i.sku

    
# for i in items_seasonV:
#     if i.list_price > 600:
#         print i.sku, i.list_price, i.season, i.id


# mtd_sales = session.query(Mtd_Sales)

# print 'from Mtd_Sales'
# for i in mtd_sales:
#     print i.sku, i.price_list_id, i.price_list.season

# item = session.query(Price_List).filter_by(id=38789)
# for i in item:
#     print i.sku, i.id

# item = session.query(Price_List).filter_by(id=84275)
# for i in item:
#     print i.sku, i.id

# for i in zapatosdama2:
#     print i.sku, i.price_list_id, i.price_list.season

