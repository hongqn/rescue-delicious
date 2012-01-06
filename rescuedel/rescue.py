#!/usr/bin/env python

import os
import sys
import sqlite3
from collections import defaultdict

from mako.template import Template

here = os.path.dirname(__file__)

class Bookmark(object):
    def __init__(self, name, url, add_date, private=False, tags=[],
                 description=''):
        self.name = name
        self.url = url
        self.add_date = add_date
        self.private = private
        self.tags = [tags]
        self.description = description

def xmlescape(s):
    buf = []
    for c in s:
        o = ord(c)
        if o > 127:
            buf.append('&#x%x;' % o)
        else:
            buf.append(c)
    return ''.join(buf)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('db', help="The ybookmarks.sqlite file in firefox "
                        "profile directory")
    parser.add_argument('output', nargs='?', default=sys.stdout,
                        help="The path to the output html file")
    args = parser.parse_args()

    conn = sqlite3.connect(args.db)
    curs = conn.cursor()
    curs.execute("select rowid, name, url, shared, description, added_date from bookmarks")
    bookmarks = dict((id, Bookmark(name=name, url=url,
                                   add_date=added_date/1000000,
                                   private=(shared != "true"),
                                   description=description))
                     for id, name, url, shared, description, added_date
                     in curs)
    curs.execute("select rowid, name from tags")
    tags = dict((id, name) for id, name in curs)
    bookmarks_tags = defaultdict(list)
    curs.execute("select bookmark_id, tag_id from bookmarks_tags")
    for bookmark_id, tag_id in curs:
        bookmarks_tags[bookmark_id].append(tag_id)

    for bookmark_id, bookmark in bookmarks.iteritems():
        bookmark.tags = [tags[tid] for tid in bookmarks_tags[bookmark_id]]

    template = Template(filename=os.path.join(here, 'delicious.mako'),
                        imports=['from rescuedel.rescue import xmlescape'],
                        output_encoding='utf-8',
                       )

    html = template.render(bookmarks=bookmarks.values())

    output = open(args.output, 'w') if isinstance(args.output, basestring) \
             else args.output

    with output as f:
        f.write(html)


if __name__ == '__main__':
    main()
