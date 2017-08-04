# -*- coding:utf-8 -*-

import sqlite3

dbname='../data/musician.db'


# データベースに接続
conn= sqlite3.connect(dbname)
c=conn.cursor()

sql_groupby='select area, count(*) from musicians group by area'
for row in c.execute(sql_groupby):
    print(row)