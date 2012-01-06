<!DOCTYPE NETSCAPE-Bookmark-file-1>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<!-- This is an automatically generated file.
It will be read and overwritten.
Do Not Edit! -->
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
%for bm in bookmarks:
<DT><A HREF="${bm.url}" ADD_DATE="${bm.add_date}" PRIVATE="${1 if bm.private else 0}" TAGS="${','.join(bm.tags)|xmlescape}">${bm.name}</A>
                        default_filters=['unicode', 'xmlescape'],
%if bm.description:
<DD>${bm.description}
%endif
%endfor
</DL><p>

