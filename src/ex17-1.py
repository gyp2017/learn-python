# -*- coding: utf-8 -*-
# 17 파일 더 다뤄 보기

from sys import argv
from os.path import exists

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file, 'r').read())
