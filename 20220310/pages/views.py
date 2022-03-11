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
    # save comment
    if 'operation_x' in request.POST.keys() and request.POST['operation_x'] == 'save_comment':
        comments_list = []
        response = 'error'
        try:
            comment = request.POST['comment'].strip()
            row_id = request.POST['row_id'].strip()
            # sql to save comment

            # sql get comments
            data_comment = {}
            data_comment['comment_id'] = 1
            data_comment['comment'] = 'comment 1'
            comments_list.append(data_comment)

            data_comment = {}
            data_comment['comment_id'] = 2
            data_comment['comment'] = comment
            comments_list.append(data_comment)

            response = 'ok'

        except Exception as ex:
            comments_list = []
            response = 'error'

        context = {
            'comments': comments_list,
            'row_id': row_id,
            'response': response,
        }
        return render(request, 'pages/comments.html', context)

    # default values
    # default values
    data = []
    # sql query
    # msql= "ASELECT ASLDAL"
    # with connection.cursor() as cursor:
    #     cursor.execute(msql)
    #     rows = cursor.fetchall()
    #     for row in rows:

    row_data = {}
    row_data['row_id'] = 1
    row_data['col1'] = '11111'  # row[0]
    row_data['col2'] = '22222'  # row[1]
    row_data['col3'] = '33333'  # row[2]
    row_data['col4'] = 'higchart'  # row[3]

    # comments
    comments = []
    # sql query
    # msql= "SQL"
    # with connection.cursor() as cursor2:
    #     cursor2.execute(msql)
    #     rows2 = cursor2.fetchall()
    #     for row2 in rows2:

    # comments
    data_comment = {}
    data_comment['comment_id'] = 1  # row2[0]
    data_comment['comment'] = 'comment 1'  # row2[1]
    comments.append(data_comment)

    row_data['col5'] = comments

    row_data['col6'] = '66666'
    row_data['col7'] = '77777'
    row_data['col8'] = '88888'

    data.append(row_data)

    # segunda fila
    row_data = {}
    row_data['row_id'] = 2
    row_data['col1'] = '11111-2'  # row[0]
    row_data['col2'] = '22222-2'  # row[1]
    row_data['col3'] = '33333-2'  # row[2]
    row_data['col4'] = 'higchart-2'  # row[3]

    # comments
    comments = []
    # sql query
    # msql= "SQL"
    # with connection.cursor() as cursor2:
    #     cursor2.execute(msql)
    #     rows2 = cursor2.fetchall()
    #     for row2 in rows2:

    # comments
    data_comment = {}
    data_comment['comment_id'] = 1  # row2[0]
    data_comment['comment'] = 'comment 1'  # row2[1]
    comments.append(data_comment)

    row_data['col5'] = comments

    row_data['col6'] = '66666-2'
    row_data['col7'] = '77777-2'
    row_data['col8'] = '88888-2'

    data.append(row_data)

    context = {
        'page': 'view1',
        'data': data,
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
