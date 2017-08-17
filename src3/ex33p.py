# -*- coding: utf-8 -*-
# 33 while문

def myWhile(end, plus):
    i = 0
    numbers = []

    while i < end:
        print "꼭대기에서 i는 %d" % i
        numbers.append(i)

        i = i + plus
        print "숫자는 이제: ", numbers
        print "바닥에서 i는 %d" % i

    return numbers

numbers = myWhile(10, 2)

print "숫자: "

for num in numbers:
    print num
