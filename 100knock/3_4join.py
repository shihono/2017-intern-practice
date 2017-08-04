# -*- coding:utf-8 -*-
import sqlite3

dbname='../data/3_1.db'

# データベースに接続
conn= sqlite3.connect(dbname)
c=conn.cursor()

# join -> groupby -> whrere
# select * from artist_tag_info inner join artist_rating_info on artist_tag_info.id = artist_rating_info.id
# select artist_rating_info.value count(*) from table group by artist_rating_info.value
# where artist_tag_info.value=’rock’