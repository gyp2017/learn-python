# -*- coding: utf-8 -*-
# 48 사용자 입력 고급

from nose.tools import *
from ex48 import parser

def test_peek():
    assert_equal(parser.peek([('direction', 'north')]), 'direction')
    result = parser.peek([('direction', 'north'),
                          ('verb', 'kill'),
                          ('direction', 'east')])
    assert_equal(result, 'direction')

def test_match():
    assert_equal(parser.match([('direction', 'north')], 'direction'), ('direction', 'north'))
    assert_equal(parser.match([('direction', 'north')], 'verb'), None)
    result = parser.match([('direction', 'north'),
                          ('verb', 'kill'),
                          ('direction', 'east')], 'direction')
    assert_equal(result, ('direction', 'north'))
    assert_equal(None, None)

def test_skip():
    word_list = [('stop', 'the'),
                 ('noun', 'princess')]
    assert_equal(parser.skip(word_list, 'stop'), None)
    assert_equal(word_list, [('noun', 'princess')])

def test_verb():
    word_list = [('stop', 'the'),
                 ('verb', 'eat'),
                 ('noun', 'princess')]
    assert_equal(parser.parse_verb(word_list), ('verb', 'eat'))

    word_list = [('verb', 'eat'),
                 ('noun', 'bear')]
    assert_equal(parser.parse_verb(word_list), ('verb', 'eat'))

    word_list = [('direction', 'south'),
                 ('noun', 'bear')]
    assert_raises(Exception, parser.parse_verb, word_list)

def test_object():
    word_list = [('stop', 'the'),
                 ('noun', 'princess')]
    assert_equal(parser.parse_object(word_list), ('noun', 'princess'))

    word_list = [('stop', 'the'),
                 ('direction', 'south')]
    assert_equal(parser.parse_object(word_list), ('direction', 'south'))

    word_list = [('verb', 'kill'),
                 ('noun', 'bear')]
    assert_raises(Exception, parser.parse_object, word_list)

def parse_subject():
    word_list = [('verb', 'eat'),
                 ('noun', 'princess')]
    sentence = parser.parse_subject(word_list, ('noun', 'bear'))
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.object, 'princess')

def test_parse_sentence():
    word_list = [('stop','the'),('noun','princess'),('verb','kill'),('noun','bear')]
    sentence = parser.parse_sentence(word_list)
    assert_equal(sentence.subject, 'princess')
    assert_equal(sentence.verb, 'kill')
    assert_equal(sentence.object, 'bear')

    word_list = [('noun','princess'),('verb','kill'),('noun','bear')]
    sentence = parser.parse_sentence(word_list)
    assert_equal(sentence.subject, 'princess')
    assert_equal(sentence.verb, 'kill')
    assert_equal(sentence.object, 'bear')

    word_list = [('verb','kill'),('noun','bear')]
    sentence = parser.parse_sentence(word_list)
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'kill')
    assert_equal(sentence.object, 'bear')

    word_list = [('direction','south'),('noun','princess')]
    assert_raises(Exception, parser.parse_sentence, word_list)
