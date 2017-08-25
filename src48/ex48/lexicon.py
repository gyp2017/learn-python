# -*- coding: utf-8 -*-

class Lexicon(object):

    dictions = {
      'direction': ['north', 'south', 'east', 'west'],
      'verb': ['go', 'kill', 'eat'],
      'stop': ['the', 'in', 'of'],
      'noun': ['bear', 'princess'],
      'number': [1234, 34536, 3]
    }

    def convert_number(self, s):
        try:
            return int(s)
        except ValueError:
            return None

    def scan(self, stuff):
        words = stuff.split()
        result = []

        for word in words:

            number = self.convert_number(word)
            if number:
                result.append(('number', number))
            else:

                isFind = False

                for key in Lexicon.dictions:
                    origins = Lexicon.dictions.get(key)

                    for origin in origins:

                        if origin == word:
                            result.append((key, word))
                            isFind = True
                            continue

                    if isFind:
                        continue

                if isFind:
                    continue
                else:
                    result.append(('error', word))

        return result
