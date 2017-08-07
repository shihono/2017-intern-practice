#!/usr/bin/python
# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tpl = env.get_template('template.html')

foods = []
foods.append({'name':u'ラーメン', 'price':400})
foods.append({'name':u'焼き飯',   'price':500})
foods.append({'name':u'天津飯',   'price':600})

html = tpl.render({'shop':u'悟空軒', 'foods':foods})
print ('Content-Type: text/html; charset=utf-8\n')
print( html.encode('utf-8'))