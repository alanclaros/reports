from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
import csv
import os

# connection to database
from django.db import connection


def index(request):
    path_file = os.path.join(settings.BASE_DIR, 'static', 'sample.csv')
    #print('path file: ', path_file)
    heads = []
    data = []
    rows_database = []

    try:
        with open(path_file) as File:
            reader = csv.reader(File, delimiter=';', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
            i = 0
            for row in reader:
                if i == 0:
                    heads.append(row[0])
                    heads.append(row[1])
                    heads.append(row[2])
                    heads.append(row[3])
                else:
                    row_data = []
                    row_data.append(row[0])
                    row_data.append(row[1])
                    row_data.append(row[2])
                    row_data.append(row[3])
                    data.append(row_data)

                i += 1

        # database
        msql = "SELECT * FROM tabla1 "
        with connection.cursor() as cursor:
            cursor.execute(msql)
            rows = cursor.fetchall()
            for row in rows:
                new_data = []
                new_data.append(row[0])
                new_data.append(row[1])
                rows_database.append(new_data)

    except Exception as ex:
        heads = []
        data = []
        rows_database = []

    context = {
        'page': 'index',
        'heads': heads,
        'data': data,
        'rows_database': rows_database,
    }

    return render(request, 'pages/index.html', context)


def view1(request):
    context = {
        'page': 'view1'
    }

    return render(request, 'pages/view1.html', context)


def view2(request):
    context = {
        'page': 'view2'
    }

    return render(request, 'pages/view2.html', context)


def view3(request):
    context = {
        'page': 'view3'
    }

    return render(request, 'pages/view3.html', context)
