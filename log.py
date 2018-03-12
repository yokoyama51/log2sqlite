
import sys
import csv
import sqlite3
from contextlib import closing
from datetime import datetime as dt



def insert_log(cursor, line) :

    sql = 'insert into log (host,user,fc,date_s,date_e,res_s,res_t,status) values (?,?,?,?,?,?,?,?)'

    try:
        d1 = dt.strptime(line[3], '%Y/%m/%d %H:%M:%S.%f')
        d2 = dt.strptime(line[4], '%Y/%m/%d %H:%M:%S.%f')
        sub = d2 - d1

        user = (line[0], line[1], line[2], line[3].replace('/', '-'), line[4].replace('/', '-'), line[5], sub.microseconds / 1000, line[6])
        cursor.execute(sql, user)

    except:
        print(id_, line)
        raise

    # 追加した行の識別キー
    return cursor.lastrowid


def insert_param(cursor, id_, param_str) :

    sql = 'insert into log_param (_id, key, value) values (?,?,?)'
    for param in param_str.split():

        # 区切り文字が無い場合はスキップ
        if param.find("=") == -1:
            continue

        try:
            v = param.split('=')
            p = (id_, (v[0].lstrip('/')), v[1])
            cursor.execute(sql, p)
        except:
            print(id_, param)



with closing(sqlite3.connect('log.sqlite3')) as conn:

    c = conn.cursor()

    with open(sys.argv[1], 'r') as f:
        reader = csv.reader(f)
        # header = next(reader)

        for line in reader:
            id_ = insert_log(c, line)
            insert_param(c, id_, line[7])

    conn.commit()
