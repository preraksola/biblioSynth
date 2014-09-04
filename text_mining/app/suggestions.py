#!/usr/bin/env python
# -*- coding: utf-8 -*-
import util
from json import dumps
from render import http_header
from query import get_cooccurrences

http_header()
args = util.get_args()
if 'term' in args:
    print dumps([{'value': st, 'co' : co} for (st, co) in get_cooccurrences(args['term'])])
else:
    print dumps([])
