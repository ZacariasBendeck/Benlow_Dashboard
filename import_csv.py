import json
import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User, Price_List, Mtd_Sales

import time
from datetime import datetime
from pprint import pprint


engine = create_engine('sqlite:///Benlow.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

wkdir = os.getcwd()
data_file  = wkdir + '/data/PRICElIST.csv'

try:
    num_rows_deleted = session.query(Price_List).delete()
    session.commit()
except:
    print 'Price_list table was not cleared!!!'
    session.rollback()

csvfile = open(data_file, 'r')
jsonfile = open('price_list.json', 'w')

fieldnames = ('SKU','Vendor SKU','Color Code','Vendor','Vendor Description',
            'Category','Category Description','Season','Season Description',
            'Size Type','Group Code','Description','Style/Color',
            'Location','List Price','Current Price','Retail Price',
            'Markdown Price 1','Markdown Price 2','Oversize Column',
            'Oversize Amount','Perks','Label Code','Coupon SKU','Keywords',
            'Picture Filename','Comments')

reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    if reader.line_num != 1:
        print row['SKU'].decode('ascii','replace').replace(" ","")
        newItem = Price_List(
            sku                 = row['SKU'].decode('ascii','replace').replace(" ",""),
            vendor_sku          = row['Vendor SKU'].decode('ascii','replace').replace(" ",""),
            color_code          = row['Color Code'].decode('ascii','replace').replace(" ",""),
            vendor              = row['Vendor'].decode('ascii','replace').replace(" ",""),
            vendor_description  = row['Vendor Description'].decode('ascii','replace').replace(" ",""),
            category            = int(row['Category'].decode('ascii','replace').replace(" ","")),
            category_description = row['Category Description'].decode('ascii','replace').replace(" ",""),
            season              = row['Season'].decode('ascii','replace').replace(" ",""),
            season_description  = row['Season Description'].decode('ascii','replace').replace(" ",""),
            group_code          = row['Group Code'].decode('ascii','replace').replace(" ",""),
            style_color         = row['Style/Color'].decode('ascii','replace').replace(" ",""),
            list_price          = row['List Price'].decode('ascii','replace').replace(" ",""),
            current_price       = row['Current Price'].decode('ascii','replace').replace(" ",""),
            picture_file        = row['Picture Filename'].decode('ascii','replace').replace(" ",""))
        session.add(newItem)





# with open(data_file1) as data_file:
#     owners = json.load(data_file)

# with open(data_file2) as data_file:
#     lists = json.load(data_file)

# with open(data_file3) as data_file:
#     items = json.load(data_file)

# pprint(lists)
# pprint(items)
# pprint(owners)



# print 'Owners added succesfully'

# for i in lists['Lists']:
#     newList = Lists(
#         name = i['name'],
#         id = i['id'],
#         description = i['description'],
#         pic_url = i['pic_url'],
#         owner_id = i['owner_id'],
#         published = datetime.today(),
#         updated = datetime.today())
#     session.add(newList)

# print 'Lists added succesfully'

# for i in items['Items']:
#     newItem = Items(
#         name = i['name'],
#         description = i['description'],
#         rank = i['rank'],
#         pic_url = i['url'],
#         lists_id = i['lists_id'],
#         published = datetime.today(),
#         updated = datetime.today())
#     print newItem.name + ' added to items'
#     session.add(newItem)

# print 'Items added succesfully'


session.commit()
session.close()
engine.dispose()
