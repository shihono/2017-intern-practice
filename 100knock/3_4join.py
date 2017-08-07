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

sql = "select * from artist_tag_info inner join artist_rating_info on artist_tag_info.id = artist_rating_info.id " \
      "where artist_tag_info.value='rock'" \
      "group by artist_rating_info.value"

for row in c.execute(sql):
    print(row)

print("***")
sql2 = "select * from artist_tag_info inner join artist_rating_info on artist_tag_info.id = artist_rating_info.id " \
      "group by artist_rating_info.value " \
      "having artist_tag_info.value='rock'"

for row in c.execute(sql2):
    print(row)
conn.close()

'''
出力結果
(1435, 1, 'rock', 1435, 4, '100')
(355223, 1, 'rock', 355223, 1, '20')
(9160, 1, 'rock', 9160, 2, '30')
(38829, 1, 'rock', 38829, 1, '40')
(87820, 1, 'rock', 87820, 5, '52')
(160, 1, 'rock', 160, 3, '53')
(2778, 1, 'rock', 2778, 4, '55')
(814709, 1, 'rock', 814709, 1, '60')
(2874, 1, 'rock', 2874, 5, '64')
(106530, 1, 'rock', 106530, 3, '67')
(151, 1, 'rock', 151, 7, '69')
(32056, 2, 'rock', 32056, 2, '70')
(1218, 1, 'rock', 1218, 5, '72')
(24459, 1, 'rock', 24459, 3, '73')
(366, 2, 'rock', 366, 4, '75')
(1146, 1, 'rock', 1146, 5, '76')
(516893, 1, 'rock', 516893, 7, '77')
(1, 2, 'rock', 1, 20, '78')
(41994, 1, 'rock', 41994, 1, '80')
(192168, 1, 'rock', 192168, 10, '82')
(985, 1, 'rock', 985, 6, '83')
(3097, 2, 'rock', 3097, 5, '84')
(35996, 2, 'rock', 35996, 4, '85')
(2990, 3, 'rock', 2990, 10, '86')
(480986, 1, 'rock', 480986, 3, '87')
(188, 1, 'rock', 188, 5, '88')
(299, 2, 'rock', 299, 11, '89')
(815, 1, 'rock', 815, 10, '90')
(1528, 2, 'rock', 1528, 9, '91')
(2121, 3, 'rock', 2121, 10, '92')
(792, 2, 'rock', 792, 3, '93')
(5794, 1, 'rock', 5794, 7, '94')
(212204, 1, 'rock', 212204, 4, '95')
(23, 1, 'rock', 23, 10, '96')
(822, 1, 'rock', 822, 6, '97')
(20143, 1, 'rock', 20143, 15, '99')
***
(1146, 1, 'rock', 1146, 5, '76')
(480986, 1, 'rock', 480986, 3, '87')
'''