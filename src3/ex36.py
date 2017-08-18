# -*- coding: utf-8 -*-
# 36 설계와 디버그

from sys import exit
from random import shuffle

Sana_Imanaga = "今永さな"
Tsubomi = "つぼみ"
Aki_Sasaki = "佐々木あき"
names = [Sana_Imanaga, Tsubomi, Aki_Sasaki]

def room(name_ko, name_jp):
    print "************************************************"
    print "%s의 방. 내 이름은 무엇일까요?" % name_ko
    shuffle(names)
    print "1. %s, 2. %s, 3. %s" % (names[0], names[1], names[2])

    next = int(raw_input(">"))

    if names[next - 1] == name_jp:
        print "정답입니다!"
        if name_ko != "아키":
            room("아키", Aki_Sasaki)
        else:
            dead("모두 맞았습니다. 방을 탈출합니다!")
    else:
        dead("틀렸습니다. 흥!!!")

def dead(why):
    print why, "잘 했어요!"
    exit(0)

def start():
    print "어두운 방에 있습니다."
    print "1사나 2츠보미 문이 있습니다."
    print "어느 쪽을 고를까요?"

    next = raw_input(">")

    if next == "1":
        room("사나", Sana_Imanaga)
    elif next == "2":
        room("츠보미", Tsubomi)
    else:
        dead("문 주위에서 맴돌기만 하다 굶어 죽었습니다.")

start()
