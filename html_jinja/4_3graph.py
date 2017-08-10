#!/usr/bin/env python
# -*- coding: utf-8 -*-


from jinja2 import Environment, FileSystemLoader
import sqlite3
import numpy as np
import matplotlib.pyplot as plt


# jinja2 テンプレートファイル
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tpl = env.get_template('template/template4_3.html')
# database
dbname='../data/3_1.db'
conn= sqlite3.connect(dbname)
c=conn.cursor()

sql_groupby ='''select id, count(value), count(count) from artist_tag_info group by id'''
graph_points =[(row[0], row[1])for row in c.execute(sql_groupby)]
conn.close()

plt.plot([point[0] for point in graph_points],[point[1] for point in graph_points])
plt.savefig("graph.png")

html = tpl.render({'title': '4_3 graph', 'image': 'graph.png'})

tmpfile = open("generate4_3.html", 'w')  # 書き込みモードで開く
tmpfile.write(html)
tmpfile.close()