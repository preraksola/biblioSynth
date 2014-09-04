#!/usr/bin/env /usr/bin/python
# -*- coding: utf-8 -*-
import render
import query
import util
import get_svg
import re

args = util.get_args() #get the form data in an array

render.http_header() #load header
render.html_header() #load scripts
gt = args['GraphTerm'] if 'GraphTerm' in args else ''
#ct = args['ClusterTerm'] if 'ClusterTerm' in args else ''
mode = args['GraphMode'] if 'GraphMode' in args else ''
render.render_div_search(ft=gt, gt=gt) #display form
#render.render_datalist( 'terms');

x = args['all'] if 'all' in args else ''

match = re.search(r'cl[0-9]',mode)

if mode == 'all' or match:
    print '''
        <p> Most Connected graph </p>
        '''
    print get_svg.get_svg_all(args)
    print '''
            </div>
            '''

if x == 'List all Terms':
   print '''
  <p> List of all terms </p>
  '''
   render.list_terms()

if gt:
    print '''
    <t3>Research of term in lexical field</t3>
    '''.format(gt=gt)
    if mode == 'text':
        print '''
        <p>Text mode, all cooccurrents</p>
        <div style="weight: 100%; height: 100%;">
        <table cellspacing = "10" align = "center">
        <tr>
        '''
        td_count = 0;
        term_count = 0;
        for (word, co) in query.get_cooccurrences(gt):
            print '''
            <td>
            <a href="/co_articles.py?FirstTerm={gt}&SecondTerm={word}">{word} {co}</a>
            </td>
            '''.format(gt=gt, word=word, co=co)
            td_count += 1
            term_count += 1
        
            if(td_count == 5):
                td_count = 0
                print '''
                    </tr>
                    <tr>
                    '''
            if (term_count == 70):
                    break
        
        print '''
        </tr>
        </table>
        </div>
        '''
    elif mode == 'simple':
        print '''
        <p>{mode} graph mode, {gt} and 70 first of its cooccurrents are linked between</p>
            '''.format(mode = mode, gt=gt)
        print get_svg.get_svg_simple(args)

    elif mode == 'complete':
        print '''
            <p>{mode} graph mode, {gt} and 70 first of its cooccurrents are linked between</p>
            '''.format(mode = mode, gt=gt)
        print get_svg.get_svg_complete(args)

    print '''
        </div>
            '''
    