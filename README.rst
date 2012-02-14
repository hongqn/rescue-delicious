=========================================================
Restore Your del.icio.us Bookmarks From Firefox Extension
=========================================================

My wife has used http://del.icio.us to store her bookmarks for years.  But she missed
the opt-in period to transfer her bookmarks from Yahoo! to AVOS, since she was
too busy taking care of our 2-year daughter and had no time to examine her
email inbox.  She got very angry today finding out that her account was deleted and
all her bookmarks have gone away.

Fortunately, she was using the `delicious extension`_ for Firefox.  This
extension syncs remote bookmarks to a local sqlite database.  So I wrote this
program to restore the bookmarks to a newly created delicious account.

.. _`delicious extension`: https://addons.mozilla.org/en-US/firefox/addon/delicious-bookmarks/

Installation
------------

::

  pip install RescueDelicious

Usage
-----

::

  rescure-delicious /path/to/ybookmarks.sqlite

The ybookmarks.sqlite file can be found in your firefox profile directory.
