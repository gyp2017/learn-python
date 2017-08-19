# -*- coding: utf-8 -*-
# 40 모듈, 클래스, 객체

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_baby = Song(["생일 축하합니다.",
                   "고소 당하기는 싫으니깐",
                   "여기서 이만 할게요"])

bull_on_parade = Song(["조개로 가득 찬 주머니 차고",
                       "가족 주위에 모여든 그들"])

happy_baby.sing_me_a_song()

bull_on_parade.sing_me_a_song()

rebirth = [
    "다시 태어난 것 같아요",
    "내 모든것이 다 달라졌어요",
    "그대를 만난 후로 난 새사람이 됐어요",
    "우리 엄마가 제일 놀라요"
]

red_velvet = Song(rebirth)

print '-' * 20
red_velvet.sing_me_a_song()
