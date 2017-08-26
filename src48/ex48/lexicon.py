# -*- coding: utf-8 -*-

dictions = {
    'direction': ['north', 'south', 'east', 'west'],
    'verb': ['go', 'kill', 'eat'],
    'stop': ['the', 'in', 'of'],
    'noun': ['bear', 'princess']
}

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(stuff):
    words = stuff.split()
    result = []

    for word in words:

        number = convert_number(word)
        if number:
            result.append(('number', number))
        else:
            isFind = False

            for key in dictions:
                origins = dictions.get(key)

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
