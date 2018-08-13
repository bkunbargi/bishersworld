#!/usr/bin/env python3
# -*#!/usr/bin/python

import cgi

def build_page():
    num = 5;
    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')
    print('<style> \
    body{ background-color: blue;          \
    } </style>')
    print('<title>Hello Word - First CGI Program</title>')
    print('</head>')
    print('<body>')
    print('<h2>Hello Word! This is my first CGI program {}</h2>'.format(num))
    form = cgi.FieldStorage()
    print('<p> {} </p>'.format(form))
    print(cgi.print_environ())

if __name__ == '''__main__''':
    build_page()
