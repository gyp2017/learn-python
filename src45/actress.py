# -*- coding: utf-8 -*-

from random import shuffle

actress = {
    'sakura_mana': {
        'name_en': 'Mana Sakura',
        'name_jp': '紗倉まな',
        'name_ko': '사쿠라 마나',
        # 생년월일
        'birth': '1993-03-23',
        # 신장
        'height': 156,
        # 신체사이즈
        'size': ['B89', 'W58', 'H89'],
        # 컵사이즈
        'cup': 'F',
        # 데뷔
        'debut': '2011-11'
    },
    'suzumura_airi': {
        'name_en': 'Airi Suzumura',
        'name_jp': '鈴村あいり',
        'name_ko': '스즈무라 아이리',
        # 생년월일
        'birth': '1993-09-24',
        # 신장
        'height': 152,
        # 신체사이즈
        'size': ['B82', 'W53', 'H80'],
        # 컵사이즈
        'cup': 'D',
        # 데뷔
        'debut': '2012-10'
    },
    'ito_chinami': {
        'name_en': 'Chinami Ito',
        'name_jp': '伊東ちなみ',
        'name_ko': '이토 치나미',
        # 생년월일
        'birth': '1996-12-01',
        # 신장
        'height': 163,
        # 신체사이즈
        'size': ['B86', 'W57', 'H86'],
        # 컵사이즈
        'cup': 'D',
        # 데뷔
        'debut': '2015-09'
    },
    'imanaga_sana': {
        'name_en': 'Sana Imanaga',
        'name_jp': '今永さな',
        'name_ko': '이마나가 사나',
        # 생년월일
        'birth': '1996-02-09',
        # 신장
        'height': 164,
        # 신체사이즈
        'size': ['B89', 'W58', 'H88'],
        # 컵사이즈
        'cup': 'G',
        # 데뷔
        'debut': '2016-06'
    }
}

def getActress(name):
    return actress.get(name)

def getPoints(point):
    answers = []

    for name in actress:
        answers.append(actress[name][point])

    shuffle(answers)
    return answers
