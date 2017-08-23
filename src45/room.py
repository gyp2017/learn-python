# -*- coding: utf-8 -*-

class QuestionRoom(object):

    keywords = {
        'name_jp': '이름',
        'birth': '생일',
        'cup': '컵'
    }

    def __init__(self, girl, answers, keyword):
        self.girl = girl
        self.answers = answers
        self.keyword = keyword

    def getQuestion(self, keyword):
        return QuestionRoom.keywords.get(keyword)

    def greeting(self):
        print "안녕하세요. 저는 '%s'라고 합니다." % self.girl['name_ko']
        print "잘 생각한 후에 정답을 맞춰주세요. 문제는 객관식 입니다."
        print "문제입니다. 저의 '%s'는 무엇일가요? 객관식 입니다." % self.getQuestion(self.keyword)
        print "\t1. %s\n\t2. %s\n\t3. %s\n\t4. %s\n" % (
            self.answers[0], self.answers[1], self.answers[2], self.answers[3])

        next = int(raw_input(">"))

        if self.answers[next - 1] == self.girl[self.keyword]:
            print "정답니다."
            return True
        else:
            print "틀렸습니다. 너무 어려웠나요?"
            return False
        
        return False



class NameRoom(QuestionRoom):

    def __init__(self, girl, answers, keyword):
        super(NameRoom, self).__init__(girl, answers, keyword)


class BirthRoom(QuestionRoom):

    def __init__(self, girl, answers, keyword):
        super(BirthRoom, self).__init__(girl, answers, keyword)

class CupRoom(QuestionRoom):

    def __init__(self, girl, answers, keyword):
        super(CupRoom, self).__init__(girl, answers, keyword)
