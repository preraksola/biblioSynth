#!/usr/bin/env python
# -*- coding: utf-8 -*-
import render
import util

args = util.get_args()
render.http_header()
render.html_header()
ft = ''
st = ''
if 'FirstTerm' in args:
    ft = args['FirstTerm']

if 'SecondTerm' in args:
    st = args['SecondTerm']
render.render_div_search(ft=ft, st=st)
#render.render_datalist( 'terms');
if 'FirstTerm' in args and 'SecondTerm' in args:
    render.render_co_articles(args['FirstTerm'], args['SecondTerm'])

