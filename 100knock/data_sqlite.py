# -*- coding:utf-8 -*-
# sqlite を使う

import json
import sqlite3

jsonname='../data/artist.json'
dbname='../data/musician.db'


# artistlistにjson　fileを格納
artistlist=[]
with open(jsonname,'r')as f:
    file=f.readlines()
    for  line in file:
        artistlist.append(json.loads(line))

# データベースに接続、connectionオブジェクトの作成
conn= sqlite3.connect(dbname)
# SQLを実行するためのcursorオブジェクトの作成
c=conn.cursor()

# executeメソッドでSQL文を実行
# create table 列名 型名
create_table= '''create table musicians (
                aliases text,
                area text,
                begin integer,
                end integer,
                gid text,
                id integer,
                name text,
                rating text,
                sort_name text,
                tags text )
                '''
c.execute(create_table)

field_set={'aliases','area','begin','end','gid','id','name','rating','sort_name','tags'}
# SQLに値をセットする
#セットしたい場所に？を記述、excuteメソッドの第二引数に？を当てはめる値をタプルに渡す
for artist in artistlist:
    column = list(field_set & set(artist.keys()))
    sql = "insert into musicians({}) values({})".format(",".join(column), ",".join(['?']*len(column)))
    musician = tuple([str(artist[key]) if (isinstance(artist[key], list)|isinstance(artist[key], dict)) else artist[key]for key in column])
    #print(sql)
    #print(list(musician))
    #print([type(m) for m in musician])
    c.execute(sql,musician)

#　変更を保存
conn.commit()
'''
select_sql = 'select * from musicians'
for row in c.execute(select_sql):
    print(row)
'''
conn.close()