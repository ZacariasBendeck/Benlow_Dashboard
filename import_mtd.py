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
data_file  = wkdir + '/data/MTDSALES.CSV'

try:
    num_rows_deleted = session.query(MTD_Sales).delete()
    session.commit()
except:
    print 'Price_list table was not cleared!!!'
    session.rollback()

csvfile = open(data_file, 'r')
jsonfile = open('price_list.json', 'w')


# Sector  SectorDesc  Dept    DeptDesc    Categ   CategDesc   SKU Description StyCol 
#  OnHand_Qty  OnHand_CurrCost OnHand_CurrCost_Val OnHand_Age  MTD_Qty MTD_Sales  
#   MTD_Mkdn_Pct    MTD_Profit  MTD_GP_Pct  MTD_ROI MTD_Turns   MTD_Orig_GP_Pct
#    MTD_Proj_GP_Pct Perks

# session.query(Price_List).all()

reader = csv.DictReader(csvfile)
for row in reader:
    if reader.line_num != 1:
        price_list = session.query(Price_List).filter_by(sku=row['SKU'].decode('ascii','replace').replace(" ","")).first()
        print price_list.sku
        print reader.line_num, 100*float(reader.line_num)/37122
        newItem = Mtd_Sales(
            sku                      = row['SKU'].decode('ascii','replace').replace(" ",""),
            price_list               = price_list,
            on_hand_qty              = int(row['OnHand_Qty'].decode('ascii','replace').replace(" ","").replace(',','')),
            on_hand_curr_cost        = float(row['OnHand_CurrCost'].decode('ascii','replace').replace(" ","").replace(',','')),
            on_hand_value            = float(row['OnHand_CurrCost_Val'].decode('ascii','replace').replace(" ","").replace(',','')),
            on_hand_age              = int(row['OnHand_Age'].decode('ascii','replace').replace(" ","")),
            mtd_qty                  = int(row['MTD_Qty'].decode('ascii','replace').replace(" ","").replace(',','')),
            mtd_sales                = float(row['MTD_Sales'].decode('ascii','replace').replace(" ","").replace(',','')),
            mtd_md_pct               = row['MTD_Mkdn_Pct'].decode('ascii','replace').replace(" ",""),
            mtd_profit               = float(row['MTD_Profit'].decode('ascii','replace').replace(" ","").replace(',','')),
            mtd_gp_pct               = row['MTD_GP_Pct'].decode('ascii','replace').replace(" ",""),
            mtd_roi                  = int(row['MTD_ROI'].decode('ascii','replace').replace(" ","")),
            mtd_turn                 = float(row['MTD_Turns'].decode('ascii','replace').replace(" ","").replace(',','')),
            sector                   = int(row['Sector'].decode('ascii','replace').replace(" ","")),
            sector_description       = row['SectorDesc'].decode('ascii','replace').replace(" ",""),
            dept                     = int(row['Dept'].decode('ascii','replace').replace(" ","")),
            dept_description         = row['DeptDesc'].decode('ascii','replace').replace(" ",""),
            category                 = int(row['Categ'].decode('ascii','replace').replace(" ","")),
            category_description     = row['CategDesc'].decode('ascii','replace').replace(" ",""))
        session.add(newItem)



session.commit()
session.close()
engine.dispose()





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


