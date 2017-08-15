# -*- coding: utf-8 -*-
# 28 불린(boolean) 연습

print '01. True and True     : %r' % (True and True)
print '02. False and True    : %r' % (False and True)
print '03. 1 == 1 and 2 == 1 : %r' % (1 == 1 and 2 == 1)
print '04. "test" == "test"  : %r' % ("test" == "test")
print '05. 1 == 1 or 2 != 1  : %r' % (1 == 1 or 2 != 1)

print "----------------------------"

print '06. True and 1 == 1     : %r' % (True and 1 == 1)
print '07. False and 0 != 0    : %r' % (False and 0 != 0)
print '08. True or 1 == 1      : %r' % (True or 1 == 1)
print '09. "test" == "testing" : %r' % ("test" == "testing")
print '10. 1 != 0 and 2 == 1   : %r' % (1 != 0 and 2 == 1)

print "----------------------------"

print '11. "test" != "testing"           : %r' % ("test" != "testing")
print '12. "test" == 1                   : %r' % ("test" == 1)
print '13. not (True and False)          : %r' % (not (True and False))
print '14. not (1 == 1 and 0 != 1)       : %r' % (not (1 == 1 and 0 != 1))
print '15. not (10 == 1 or 1000 == 1000) : %r' % (not (10 == 1 or 1000 == 1000))

print "----------------------------"

print '16. not (1 != 10 or 3 == 4)                                      : %r' % (
  not (1 != 10 or 3 == 4))
print '17. not ("testing" == "testing" and "Zed"  == "Cool Guy")        : %r' % (
  not ("testing" == "testing" and "Zed"  == "Cool Guy"))
print '18. 1 == 1 and not ("testing" == 1 or 1 == 0)                    : %r' % (
  1 == 1 and not ("testing" == 1 or 1 == 0))
print '19. "chunky" == "bacon" and not (3 == 4 or 3 == 3)               : %r' % (
  "chunky" == "bacon" and not (3 == 4 or 3 == 3))
print '20. 3 != 4 and not ("testing" != "test" or "Python" == "Python") : %r' % (
  3 != 4 and not ("testing" != "test" or "Python" == "Python"))
