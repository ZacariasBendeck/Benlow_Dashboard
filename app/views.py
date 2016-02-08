from app import app
from flask import Flask, render_template, url_for, request
from flask import redirect, flash, jsonify
from app.import_file_helpers import *
from app.decorators import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import session as login_session

from models import Base, User, Price_List, Mtd_Sales


import csv, os

print 'The server has reloaded!!!'

engine = create_engine('sqlite:///Benlow.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

SEASONS = ['Q','R','S','T','U','V','W','X']

# header, data = import_file('ZAPATOSDAMA.CSV')
# vendor_header, vendor_data = import_file('VENDORMTDVSPRIOR.CSV')
# # data1, data2 = import_file_sort_top_10('DEPARTMENTMTDVSPRIOR.CSV')


dept_by_month = []
data_file = open('data/PROFITDAMAS.CSV')
data_file_reader = csv.reader(data_file)
for row in data_file_reader:
    if data_file_reader.line_num == 1:
        dept_header = row
    elif data_file_reader.line_num not in [2,3,16]:
        dept_by_month.append(row)



@app.route("/")
@app.route('/index')
def index():
    return render_template('welcome.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404

# - - - - - - - - SECCION ZACARIAS - - - - - - - - - - - - - - - -


@app.route("/datatables")
@login_required
def datatables():
    header, data = import_file('data/ZAPATOSDAMA.CSV')
    price_list = session.query(Price_List).all()
    for i in price_list:
        print i.season
    return render_template('datatables.html', data=data,
                header=header, price_list=price_list,
                scripts='tables_scripts')

@app.route("/hchartable")
def hchartable():
    vendor_header, vendor_data = import_file('data/VENDORMTDVSPRIOR.CSV')
    header2, data2 = import_dept_by_month('data/ZAPATOSDAMA.CSV')
    return render_template('hchartable.html',
        data=vendor_data, header=vendor_header,
        data2=dept_by_month, header2=dept_header,
        scripts=hchartable)

@app.route("/MTDZapatoM")
def MTDZapatoM():
    title = 'MONTH TO DATE ZAPATO DE MARCA HOMBRE'
    data = session.query(Mtd_Sales).join(Price_List)\
    .filter(Mtd_Sales.category.between(121,139))\
    .filter(Price_List.season.in_(SEASONS)).all()
    return render_template('datatables2.html',
        data=data, type='MTD',
        scripts='tables_scripts',
        title=title)

@app.route("/MTDDeportivoM")
def MTDDeportivoM():
    title = 'MONTH TO DATE ZAPATO DEPORTIVO DE MARCA HOMBRE'
    data = session.query(Mtd_Sales).join(Price_List)\
        .filter(Mtd_Sales.category.between(141,145))\
        .filter(Price_List.season.in_(SEASONS)).all()
    return render_template('datatables2.html',
        data=data, type='MTD', scripts='tables_scripts',
        title=title)

@app.route("/MTDZapatoMM")
def MTDZapatoMM():
    title = 'MONTH TO DATE ZAPATO DE MARCA MUJER'
    data = session.query(Mtd_Sales).join(Price_List)\
        .filter(Mtd_Sales.category.between(161,179))\
        .filter(Price_List.season.in_(SEASONS)).all()
    return render_template('datatables2.html',
        data=data, type='MTD', scripts='tables_scripts',
        title=title)

@app.route("/MTDDeportivoMM")
def MTDDeportivoMM():
    title = 'MONTH TO DATE ZAPATO DEPORTIVO DE MARCA MUJER'
    data = session.query(Mtd_Sales).join(Price_List)\
        .filter(Mtd_Sales.category.between(146,149))\
        .filter(Price_List.season.in_(SEASONS)).all()
    data = session.query(Mtd_Sales).filter(Mtd_Sales.category.between(146,149))
    return render_template('datatables2.html',
        data=data, type='MTD', scripts='tables_scripts',
        title=title)

@app.route("/MTDDeportivos")
def WTDDeportivos():
    title = 'MONTH TO DATE DEPORTIVO DE DAMA'
    data = session.query(Mtd_Sales).join(Price_List)\
        .filter(Mtd_Sales.category==556)\
        .filter(Price_List.season.in_(SEASONS)).all()
    return render_template('datatables2.html',
        data=data, type='MTD',
        scripts='tables_scripts',
        title=title)

@app.route("/MTDFlats")
def MTDFlats():
    title = 'MONTH TO DATE FLATS DE DAMA'
    data = session.query(Mtd_Sales).join(Price_List)\
        .filter(Mtd_Sales.category.between(557,565))\
        .filter(Price_List.season.in_(SEASONS)).all()
    return render_template('datatables2.html',
        data=data, type='MTD',
        scripts='tables_scripts',
        title=title)

@app.route("/MTDTacones")
def MTDTacones():
    title = 'MONTH TO DATE TACONES DE DAMA'
    data = session.query(Mtd_Sales).join(Price_List)\
        .filter(Mtd_Sales.category.between(566,575))\
        .filter(Price_List.season.in_(SEASONS)).all()
    return render_template('datatables2.html',
        data=data, type='MTD',
        scripts='tables_scripts',
        title=title)

@app.route("/MTDTaconCorrido")
def MTDTaconCorrido():
    title = 'MONTH TO DATE TACON CORRIDO DE DAMA'
    data = session.query(Mtd_Sales).join(Price_List)\
        .filter(Mtd_Sales.category.between(576,584))\
        .filter(Price_List.season.in_(SEASONS)).all()
    return render_template('datatables2.html',
        data=data, type='MTD',
        scripts='tables_scripts',
        title=title)

@app.route("/MTDSandalias")
def MTDSandalias():
    title = 'MONTH TO DATE SANDALIAS DE DAMA'
    data = session.query(Mtd_Sales).filter(Mtd_Sales.category.between(576,584))
    return render_template('datatables2.html',
        data=data, type='MTD',
        scripts='tables_scripts',
        title=title)

@app.route("/MTDBotas")
def MTDBotas():
    title = 'MONTH TO DATE BOTAS DE DAMA'
    data = session.query(Mtd_Sales).join(Price_List)\
        .filter(Mtd_Sales.category.between(591,595))\
        .filter(Price_List.season.in_(SEASONS)).all()
    return render_template('datatables2.html',
        data=data, type='MTD',
        scripts='tables_scripts',
        title=title)

@app.route("/MTDZapatoFiesta")
def MTDZapatoFiesta():
    title = 'MONTH TO DATE ZAPATO DE FIESTA DE DAMA'
    data = session.query(Mtd_Sales).join(Price_List)\
        .filter(Mtd_Sales.category.between(596,599))\
        .filter(Price_List.season.in_(SEASONS)).all()
    return render_template('datatables2.html',
        data=data, type='MTD',
        scripts='tables_scripts',
        title=title)

@app.route("/justdatatables")
def justdatatables():
    header, data = import_file('data/MAMIMTDU.CSV')
    title = 'MONICA TEMPORADA U OTONO 2015'
    return render_template('datatables.html',
        data=data, type='MTD', header = header,
        scripts='tables_scripts',
        title=title)



@app.route("/monicadatatables")
def monicadatatables():
    header, data = import_file('data/REPORTEMAMI.CSV')
    return render_template('datatables.html', data=data,
                header=header,
                scripts='tables_scripts')


@app.route("/monicadatatablesU")
def monicadatatablesU():
    header, data = import_file('data/MAMIMTDU.CSV')
    title = 'MONICA TEMPORADA U OTONO 2015'
    return render_template('datatables.html',
                data=data, header=header,
                scripts='tables_scripts',
                title=title)

@app.route("/monicadatatablesV")
def monicadatatablesV():
    header,data = import_file('data/MAMIMTDV.CSV')
    title = 'MONICA TEMPORADA V NAVIDAD 2015'
    return render_template('datatables.html',
                data=data, header=header,
                scripts='tables_scripts',
                title=title)




@app.route("/applayout")
def applayout():
    return render_template('applayout.html')

@app.route("/blank_")
def blank_():
    return render_template('blank_.html')

@app.route("/base")
def base():
    return render_template('base.html')


# @app.route("/datatables2")
# def datatables2():
#     title = 'MONTH TO DATE ZAPATO DE MARCA HOMBRE'
#     return render_template('datatables2.html',
#         scripts='tables_scripts')
