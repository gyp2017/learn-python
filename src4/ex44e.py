# -*- coding: utf-8 -*-
# 44.5 합성

class Other(object):

    def implicit(self):
        print "다른 implicit()"

    def override(self):
        print "다른 override()"

    def altered(self):
        print "다른 altered()"

class Child(object):

    def __init__(self, other):
        self.other = other

    def implicit(self):
        self.other.implicit()

    def override(self):
        self.other.override()

    def altered(self):
        print "자식, 다른 altered() 호출 전"
        self.other.altered()
        print "자식, 다른 altered() 호출 후"

other = Other()
son = Child(other)

son.implicit()
son.override()
son.altered()

