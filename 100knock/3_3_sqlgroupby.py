# -*- coding:utf-8 -*-
# artist_tag_info においてgroupby
import sqlite3

dbname='../data/3_1.db'


# データベースに接続
conn= sqlite3.connect(dbname)
c=conn.cursor()

sql_groupby='select id, count(value), count(count) from artist_tag_info group by id'
for row in c.execute(sql_groupby):
    print(row)
conn.close()

'''
出力結果
1, 178, 178)
(4, 16, 16)
(6, 9, 9)
(7, 1, 1)
(9, 2, 2)
(10, 2, 2)
(11, 3, 3)
(12, 2, 2)
(15, 2, 2)
(16, 1, 1)
(17, 24, 24)
(18, 8, 8)
......
(1197878, 7, 7)
(1197899, 14, 14)
(1197945, 5, 5)
(1197971, 2, 2)
(1197975, 16, 16)
(1197981, 5, 5)
(1198180, 3, 3)
'''