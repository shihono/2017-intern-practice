# -*- coding:utf-8 -*-
# 3.2　レコード検索

import sqlite3

dbname='../data/musician.db'


# データベースに接続
conn= sqlite3.connect(dbname)
# SQLを実行するためのcursorオブジェクト
c=conn.cursor()

# SELECT WHERE で検索
select_sql = 'select * from musicians where name=?'
search_name = ('Oasis', )
for row in c.execute(select_sql,search_name):
    print(row)

conn.close()

'''
出力結果
(None, 'United Kingdom', None, None, None, 'a7a848c3-515d-4486-9e69-dc7491dd3bd1', 377879, 'Oasis', None, 'Oasis', "[{'value': 'morning glory', 'count': 1}, {'value': 'oasis', 'count': 1}]")
(None, 'United States', None, None, None, 'ecf9f3a3-35e9-4c58-acaa-e707fba45060', 286198, 'Oasis', None, 'Oasis', None)
("[{'name': 'OASIS', 'sort_name': 'OASIS'}, {'name': 'オアシス', 'sort_name': 'オアシス'}]", 'United Kingdom', "{'year': 1991}", "{'date': 28, 'month': 8, 'year': 2009}", None, '39ab1aed-75e0-4140-bd47-540276886b60', 20660, 'Oasis', "{'value': 86, 'count': 13}", 'Oasis', "[{'value': 'rock', 'count': 1}, {'value': 'britpop', 'count': 3}, {'value': 'british', 'count': 4}, {'value': 'uk', 'count': 1}, {'value': 'britannique', 'count': 1}, {'value': 'rock and indie', 'count': 1}, {'value': 'england', 'count': 1}, {'value': 'manchester', 'count': 1}]")
(None, 'United Kingdom', None, None, None, 'a7a848c3-515d-4486-9e69-dc7491dd3bd1', 377879, 'Oasis', None, 'Oasis', "[{'count': 1, 'value': 'morning glory'}, {'count': 1, 'value': 'oasis'}]")
(None, 'United States', None, None, None, 'ecf9f3a3-35e9-4c58-acaa-e707fba45060', 286198, 'Oasis', None, 'Oasis', None)
("[{'name': 'OASIS', 'sort_name': 'OASIS'}, {'name': 'オアシス', 'sort_name': 'オアシス'}]", 'United Kingdom', "{'year': 1991}", "{'date': 28, 'year': 2009, 'month': 8}", None, '39ab1aed-75e0-4140-bd47-540276886b60', 20660, 'Oasis', "{'count': 13, 'value': 86}", 'Oasis', "[{'count': 1, 'value': 'rock'}, {'count': 3, 'value': 'britpop'}, {'count': 4, 'value': 'british'}, {'count': 1, 'value': 'uk'}, {'count': 1, 'value': 'britannique'}, {'count': 1, 'value': 'rock and indie'}, {'count': 1, 'value': 'england'}, {'count': 1, 'value': 'manchester'}]")

'''