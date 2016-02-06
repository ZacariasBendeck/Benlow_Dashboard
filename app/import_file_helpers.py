import csv, os
from operator import itemgetter, attrgetter
import pprint
import unicodedata


pp = pprint.PrettyPrinter()

def import_file(filename):
    data = []
    report_info = []
    header = []
    last_line = ''
    data_file = open(filename)
    data_file_reader = csv.reader(data_file)
    for row in data_file_reader:
        if data_file_reader.line_num != 1:
            for item in row:
                item.encode('ascii','ignore')
            data.append(row)
        else:
            header = row
        last_line = data_file_reader.line_num

    print filename + ' was imported succesfully'
    print str(last_line) + ' lines were imported!'

    return header, data

def import_dept_by_month(filename):
    dept_by_month = []
    data_file = open(filename)
    data_file_reader = csv.reader(data_file)
    for row in data_file_reader:
        if data_file_reader.line_num == 1:
            dept_header = row
        elif data_file_reader.line_num not in [2,3,16]:
            dept_by_month.append(row)
    return dept_header, dept_by_month


# def import_file_sort_top_10(filename):
    # # print dataf.head()
    # data = []
    # data_file = open(filename)
    # data_file_reader = csv.reader(data_file)
    # for row in data_file_reader:
    #     if data_file_reader.line_num != 1:
    #         data.append(row)
    #     else:
    #         header = row
    # print filename + ' was imported succesfully'
    # sorted(data, key=itemgetter(9))
    # data = data[:10]
    # print '********PRINTING FIRST 10 ROWS    ************'
    # pp.pprint(data)

    # return header, data

