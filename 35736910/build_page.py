#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import os

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def create_html_doc():
    page_title = 'Using Python3 and Selenium to gather table data'

    numba_list = []
    start_numba = 111111111
    for n in range(9):
        numba_list.append("{:,}".format(start_numba))
        start_numba += 111111111

    j2_base = Environment(loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True)
    rendered_page = j2_base.get_template('base.html').render(
        title=page_title, numbas=numba_list
    )

    f = open('html/index.html', 'a')
    f.write(rendered_page.encode('utf8'))
    f.close()

if __name__ == '__main__':
    create_html_doc()
