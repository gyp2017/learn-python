# -*- coding: utf-8 -*-
# 17 파일 더 다뤄 보기

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "%s에서 %s로 복사합니다." % (from_file, to_file)

#
in_file = open(from_file, 'r')
indata = in_file.read()

print "입력 파일은 %d바이트 입니다." % len(indata)

print "출력 파일이 존재하나요? %r" % exists(to_file)
print "준비되었습니다. 계속하려면 리턴 키를, 취소하려면 CTRL-C를 누르세요"
raw_input('?')

out_file = open(to_file, 'w')
out_file.write(indata)

print "좋습니다. 모두 완료되었습니다."

out_file.close()
in_file.close()
