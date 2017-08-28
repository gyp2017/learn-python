# -*- coding: utf-8 -*-

from ex48 import lexicon
from ex48 import parser

# print lexicon.scan("north")

# def test_skip():
#     word_list = [('noun', 'princess'),
#                  ('verb', 'kill'),
#                  ('stop', 'the'),
#                  ('noun', 'bear')]
#     parser.skip(word_list, 'stop')

#     print word_list

# test_skip()

# def test_verb():
#     print "test_verb"
#     word_list = [('stop', 'the'),
#                  ('verb', 'eat'),
#                  ('noun', 'princess')]
#     print parser.parse_verb(word_list)

# test_verb()

def parse_subject():
    word_list = [('verb', 'eat'),
                 ('noun', 'princess')]

    sentence = parser.parse_subject(word_list, ('noun', 'bear'))
    print sentence.subject
    print sentence.verb
    print sentence.object

parse_subject()
