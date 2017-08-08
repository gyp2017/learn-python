# -*- coding: utf-8 -*-
# 10 그거 뭐였죠?

tabby_cat = "\t난 탭이 됨."
persian_cat = "나는\n분리됨."
backslash_cat = "나는 \\ 고 \\ 양이"

fat_cat = """
할 일 목록:
\t* 고양이밥
\t* 물고기
\t* 개박하\n\t* 오리새
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "%r <- %%r" % tabby_cat
print "%s <- %%s" % tabby_cat
