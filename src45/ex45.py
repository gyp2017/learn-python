# -*- coding: utf-8 -*-

from sys import exit
import room
import actress

class Engine(object):

    map_questions = [
        {
            'actress': 'suzumura_airi',
            'keyword': 'name_jp'
        },
        {
            'actress': 'ito_chinami',
            'keyword': 'birth'
        },
        {
            'actress': 'imanaga_sana',
            'keyword': 'cup'
        },
        {
            'actress': 'sakura_mana',
            'keyword': 'cup'
        }
    ]

    def __init__(self):
        print "게임 엔진 초기화 중..."

        self.rooms = []

        for question in Engine.map_questions:
            a_actress = actress.getActress(question['actress'])
            a_answers = actress.getPoints(question['keyword'])
            a_room = room.QuestionRoom(a_actress, a_answers, question['keyword'])
            self.rooms.append(a_room)

        self.rooms.reverse()

    def play(self):
        print "게임을 시작합니다."

        while True:

            room = self.rooms.pop()
            result = room.greeting()
            if result == True and len(self.rooms) > 0:
                print "다음 방으로 진행합니다."
            elif result == True:
                print "방 탈출에 성공 했어요. !!!"
                return exit(0)
            else:
                print "방 탈출에 실패 했네요. ㅠㅠ"
                return exit(0)

av_game = Engine()
av_game.play()
