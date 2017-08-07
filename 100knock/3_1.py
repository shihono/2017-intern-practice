# -*- coding:utf-8 -*-
# databaseの作成

import json
import sqlite3

json_name ='../data/artist.json'
db_name ='../data/3_1.db'


# artist list にjson　fileを格納
artist_list =[]
with open(json_name,'r')as f:
    file = f.readlines()
    for line in file:
        artist_list.append(json.loads(line))

# データベースに接続、connectionオブジェクトの作成
conn= sqlite3.connect(db_name)
# SQLを実行するためのcursorオブジェクトの作成
c=conn.cursor()

print("input database")

# artist_basic_info
c.execute('''create table artist_basic_info(
            id  INTEGER,
            sort_name TEXT)''')

c.execute('create index nameindex on artist_basic_info(sort_name)')

# artist_tag_info
c.execute('''create table artist_tag_info(
            id INTEGER,
            count INTEGER,
            value TEXT)''')
# artist_rating_info
c.execute('''create table artist_rating_info(
            id INTEGER,
            count INTEGER,
            value TEXT)''')

# sqlにデータ書き込み
for artist in artist_list:
    artist_info = (int(artist["id"]), artist["sort_name"])
    c.execute('insert into artist_basic_info (id,sort_name) values(?,?)', artist_info)
    if "tags" in artist.keys():
        # tagはlistで格納されている
        tag_list = [(int(artist["id"]), int(tag["count"]), tag["value"]) for tag in artist["tags"]]
        c.executemany('insert into artist_tag_info (id, count, value) values (?,?,?)', tag_list)

    if "rating" in artist.keys():
        rating = (int(artist["id"]), artist["rating"]["count"], artist["rating"]["value"])
        c.execute('insert into artist_rating_info (id, count, value) values (?,?,?)', rating)

conn.commit()

print("create 3_1.db")
conn.close()