#!/usr/bin/env python
# -*- coding: utf-8 -*-
# database のレコードを表示

from jinja2 import Environment, FileSystemLoader
import sqlite3

# jinja2 テンプレートファイル
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tpl = env.get_template('template/template4_2.html')

# データベース
dbname='../data/3_1.db'
conn= sqlite3.connect(dbname)
c=conn.cursor()

artist_list =[]
for row in c.execute("select * from artist_basic_info"):
    artist_list.append({'id':row[0], 'name':row[1]})

# テンプレートへの挿入
html = tpl.render({'title': '4_2 table', 'record_list': artist_list})
#print(html)

# ファイルへの書き込み
# encodeする必要がない？
tmpfile = open("generate4_2.html", 'w')  # 書き込みモードで開く
tmpfile.write(html)
tmpfile.close()