#!/usr/bin/env python

import cgi

print "Content-type: text/html"
print
print "<title>Test CGI</title>"
print "<p>Hello World!</p>"
form = cgi.FieldStorage()
print "<p> {} </p>".format("caca" in form)
for key in form:
    print '<p>{} -> {}</p>'.format(key, form[key].value)
