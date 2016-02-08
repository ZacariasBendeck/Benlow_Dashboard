import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import render_template
from flask import send_from_directory
from app import app
from app.import_file_helpers import *
from app.decorators import *
from database_setup import Base


print('The server has reloaded!!!')

engine = create_engine('sqlite:///dashboardBenlow.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# header, data = import_file('ZAPATOSDAMA.CSV')
# vendor_header, vendor_data = import_file('VENDORMTDVSPRIOR.CSV')
# # data1, data2 = import_file_sort_top_10('DEPARTMENTMTDVSPRIOR.CSV')


dept_by_month = []
data_file = open('data/PROFITDAMAS.CSV')
data_file_reader = csv.reader(data_file)
for row in data_file_reader:
    if data_file_reader.line_num == 1:
        dept_header = row
    elif data_file_reader.line_num not in [2, 3, 16]:
        dept_by_month.append(row)


@app.route("/")
@app.route('/index')
def index():
    return render_template('welcome.html')


@app.route('/media/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


@app.route("/datatables")
def datatables():
    header, data = import_file('data/ZAPATOSDAMA.CSV')
    return render_template(
        'datatables.html', data=data,
        header=header,
        scripts='tables_scripts')


@app.route("/hchartable")
def hchartable():
    vendor_header, vendor_data = import_file('data/VENDORMTDVSPRIOR.CSV')
    header2, data2 = import_dept_by_month('data/ZAPATOSDAMA.CSV')
    return render_template(
        'hchartable.html',
        data=vendor_data, header=vendor_header,
        data2=dept_by_month, header2=dept_header,
        scripts=hchartable)


@app.route("/monicadatatables")
def monicadatatables():
    header, data = import_file('data/REPORTEMAMI.CSV')
    return render_template('datatables.html', data=data, header=header, scripts='tables_scripts')


@app.route("/monicadatatablesU")
def monicadatatablesU():
    header, data = import_file('data/MAMIMTDU.CSV')
    title = 'MONICA TEMPORADA U OTONO 2015'
    return render_template(
        'datatables.html', data=data, header=header, scripts='tables_scripts', title=title)


@app.route("/monicadatatablesV")
def monicadatatablesV():
    header, data = import_file('data/MAMIMTDV.CSV')
    title = 'MONICA TEMPORADA V NAVIDAD 2015'
    return render_template(
        'datatables.html', data=data, header=header, scripts='tables_scripts', title=title)


@app.route("/applayout")
def applayout():
    return render_template('applayout.html')


@app.route("/blank_")
def blank_():
    return render_template('blank_.html')


@app.route("/base")
def base():
    return render_template('base.html')
