#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
from datetime import datetime

# テンプレートファイルを指定
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tpl = env.get_template('template/template.html')

# テンプレートへ挿入するデータの作成
time = datetime.now()

# テンプレートへの挿入
html = tpl.render({'time': time})
print(html)

# ファイルへの書き込み
# encodeする必要がない？
tmpfile = open("generate.html", 'w')  # 書き込みモードで開く
tmpfile.write(html)
tmpfile.close()