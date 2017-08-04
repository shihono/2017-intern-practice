# -*- coding:utf-8 -*-
# 3.2　レコード検索
# 変更：　3_1.dbの artist_basic_infoにおいて検索する

import sqlite3

dbname='../data/3_1.db'


# データベースに接続
conn= sqlite3.connect(dbname)
# SQLを実行するためのcursorオブジェクト
c=conn.cursor()

# SELECT WHERE で検索
select_sql = 'select * from artist_basic_info where sort_name=?'
search_name = ('Oasis', )
for row in c.execute(select_sql,search_name):
    print(row)

conn.close()

'''
出力結果
(377879, 'Oasis')
(286198, 'Oasis')
(20660, 'Oasis')
(965573, 'Oasis')

'''