# -*- coding:utf-8 -*-
# sqlite を使う
# WIP
import json
import sqlite3

jsonname='data/artist.json'
dbname='data/musician.db'

traffic=json.load(open(jsonname))

# データベースに接続、connectionオブジェクトの作成
conn= sqlite3.connect(dbname)
# SQLを実行するためのcursorオブジェクトの作成
c=conn.cursor()

# executeメソッドでSQL文を実行
create_table= '''create table users (id int, name varchar(64),
                age int , gender varchar(32)'''
c.execute(create_table)


# SQLに値をセットする
#セットしたい場所に？を記述、excuteメソッドの第二引数に？を当てはめる値をタプルに渡す
sql= 'insert into users'
user=()
c.execute(sql,user)

# 複数のsqlを実行するときはタプルのリストを作成、excutemanyメソッドを実行
insert_sql='insert into users'
users=[(),()]
c.executemany(insert_sql,users)
conn.commit()

