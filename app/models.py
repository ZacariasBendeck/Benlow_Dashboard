import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

### CLASS Code ###
class  User(Base):
    ### TABLE INFORMATION ###
    __tablename__ = 'users'

    ### MAPPERS ###
    name            = Column(String(80), nullable = False)
    email           = Column(String(250), nullable = False)
    pic_url         = Column(String(1000))
    created         = Column(String(100))
    updated         = Column(String(100))
    permission_level = Column(String(100))
    extra_col_1     = Column(String(100))
    extra_col_2     = Column(String(100))
    id              =  Column(Integer, primary_key = True)

    @property
    def serialize(self):
        return {
        'name' : self.name,
        'email' : self.email,
        'pic_url': self.pic_url,
        "created" : self.created,
        "updated" : self.updated,
        'id': self.id
        }

### CLASS Code ###
class  Price_List(Base):
    ### TABLE INFORMATION ###
    __tablename__ = 'price_list'

    ### MAPPERS ###
    sku = Column(String(80), nullable = False)
    vendor_sku          = Column(String(30))
    color_code          = Column(String(30))
    vendor              = Column(String(30))
    vendor_description  = Column(String(30))
    category            = Column(Integer)
    category_description = Column(String(30))
    season              = Column(String(30))
    season_description  = Column(String(30))
    group_code          = Column(String(30))
    style_color         = Column(String(30))
    list_price          = Column(Float(30))
    current_price       = Column(Float(30))
    picture_file        = Column(String(30))
    id                  = Column(Integer, primary_key = True)

### CLASS Code ###
class  Mtd_Sales(Base):
    ### TABLE INFORMATION ###
    __tablename__ = 'mtd_sales'

    ### MAPPERS ###
    sku                 = Column(String(30), nullable = False)
    on_hand_qty         = Column(Integer)
    on_hand_curr_cost   = Column(Float(30))
    on_hand_value       = Column(Float(30))
    on_hand_age         = Column(Integer)
    mtd_qty             = Column(Integer)
    mtd_sales           = Column(Float(30))
    mtd_md_pct          = Column(String(30))
    mtd_profit          = Column(Float(30))
    mtd_gp_pct          = Column(String(30))
    mtd_roi             = Column(Integer)
    mtd_turn            = Column(Float(30))
    sector              = Column(Integer)
    sector_description  = Column(String(50))
    dept                = Column(Integer)
    dept_description    = Column(String(30))
    category            = Column(Integer)
    category_description= Column(String(30))
    price_list_id = Column(Integer, ForeignKey('price_list.id'))
    price_list = relationship(Price_List)
    id                  = Column(Integer, primary_key = True)




#     @property
#     def serialize(self):
#         return {
#         'name' : self.name,
#         'description' : self.description,
#         'list_type' : self.list_type,
#         'pic_url': self.pic_url,
#         'id': self.id,
#         'owner_id' : self.owner_id,
#         "published" : self.published,
#         "updated" : self.updated
#         }


# ### CLASS CODE ##
# class Items(Base):  ### classes in camelcase
#     ### TABLE INFORMATION
#     __tablename__ = 'items'  ## table names in lowercase

#     ###  MAPPER CODE
#     name = Column(String(90), nullable = False)
#     id = Column(Integer, primary_key = True)
#     url = Column(String(250))
#     description = Column(String(250))
#     rank = Column(Integer)
#     pic_url = Column(String(250))
#     second_pic_url = Column(String(250))
#     essay = Column(String(10000))
#     published = Column(String(100))
#     updated = Column(String(100))

#     lists_id = Column(Integer, ForeignKey('lists.id'))
#     lists = relationship(Lists)

#     @property
#     def serialize(self):
#         return {
#         'name' : self.name,
#         'description' : self.description,
#         'id' : self.id,
#         'pic_ url': self.pic_url,
#         'url' : self.url,
#         'rank': self.rank,
#         'lists_id': self.lists_id,
#         'essay': self.essay,
#         'rank' : self.rank,
#         "published" : self.published,
#         "updated" : self.updated
#         }

########insert at the end of the file  ###############
#####
engine = create_engine('sqlite:///Benlow.db')

Base.metadata.create_all(engine)