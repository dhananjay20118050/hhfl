from django.shortcuts import render, redirect

from RPAPanel.views import indexdatacapture
from .models import upload_file
from .forms import uploadFileForm
from django.http import HttpResponse
from django.db import models, connections
import csv
from django.contrib import messages

from django.db.utils import OperationalError

db_conn = connections['datacapture_db']
try:
    c = db_conn.cursor()
except OperationalError:
    connected = False
else:
    connected = True

curs = db_conn.cursor()


def insert_file(request):
    if request.method == 'POST':
        # filename.endswith('.csv'):
        fileData = uploadFileForm(request.POST, request.FILES)
        if request.FILES:
            filename = request.FILES['file'].name
            if filename.endswith('.csv'):
                fname = handle_uploaded_file(request.FILES['file'])
                sql = "INSERT INTO bot_uploaded_files (file_name, user_id) VALUES (%s, %s)"
                val = (fname, 2)
                curs.execute(sql, val)
                batchID = curs.lastrowid
                # csv start
                fields = []
                validRows = []
                duplicateRows = []
                suc_cnt = 0
                fail_cnt = 0
                # filename = "static/upload/test_csv.csv"
                filename = 'static/upload/' + fname
                with open(filename, 'r') as csvfile:
                    csvreader = csv.reader(csvfile)
                    fields = next(csvreader)
                    for row in csvreader:
                        curs.execute("SELECT COUNT(*) from bot_aps_tracking where AppFormNo='" + row[0] + "'")
                        result = curs.fetchone()
                        # return HttpResponse(curs._last_executed)
                        if (result[0] == 0):
                            row.append(batchID)
                            validRows.append(row)
                            suc_cnt += 1
                        else:
                            duplicateRows.append(row)
                            fail_cnt += 1
                sql = "INSERT INTO bot_aps_tracking(AppFormNo,apsNo,batchId) VALUES (%s,%s,%s)"
                curs.executemany(sql, validRows)
                messages.success(request,
                                 'file uploaded successfuly. Success : ' + str(suc_cnt) + ' Duplicate : ' + str(
                                     fail_cnt))
                if (suc_cnt == 0):
                    sql = "DELETE FROM bot_uploaded_files WHERE id = " + str(batchID)
                    curs.execute(sql)
                return redirect('/datacapture/', request)
                # return indexapps(request)
            else:
                messages.error(request, 'Please upload only CSV files.')
                return redirect('/datacapture/', request)
                # return indexapps(request)
        else:
            messages.error(request, 'Please Select CSV files.')
            return redirect('/datacapture/', request)
    else:
        return redirect('/datacapture/', request)


def handle_uploaded_file(f):
    with open('static/upload/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return f.name
