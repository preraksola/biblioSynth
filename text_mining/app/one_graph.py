#!/usr/bin/env /usr/bin/python
# -*- coding: utf-8 -*-

import render
import get_svg
import util


args = util.get_args()
render.http_header()
gt = args['GraphTerm'] if 'GraphTerm' in args else ''
mode = args['GraphMode'] if 'GraphMode' in args else ''

print get_svg.get_svg(args)
print get_svg.get_svg_all(args)
