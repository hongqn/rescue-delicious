#!/usr/bin/env python

import os
import sqlite3
from collections import defaultdict
from getpass import getpass
from datetime import datetime
import time

from pydelicious  import DeliciousAPI

class Bookmark(object):
    def __init__(self, name, url, add_date, private=False, tags=[],
                 description=''):
        self.name = name
        self.url = url
        self.add_date = datetime.fromtimestamp(add_date)
        self.private = private
        self.tags = [tags]
        self.description = description

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('db', help="The ybookmarks.sqlite file in firefox "
                        "profile directory")
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

    for bookmark_id, bookmark in bookmarks.items():
        bookmark.tags = [tags[tid] for tid in bookmarks_tags[bookmark_id]]

    api = DeliciousAPI(raw_input("username: "), getpass("password: "))
    for bm in bookmarks.values():
        print "Posting %s" % bm.name
        api.posts_add(url=bm.url, description=bm.name,
                      extended=bm.description, tags=','.join(bm.tags),
                      dt=bm.add_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
                      replace=True,
                      shared=not bm.private)
        time.sleep(1)


if __name__ == '__main__':
    main()
