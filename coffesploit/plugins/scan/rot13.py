# -*- coding: utf-8 -*-
letters = [chr(i) for i in xrange(ord('a'), ord('z') + 1)]

def rot13_letter(letter):
    if letter.isalpha():
        return letters[(letters.index(letter.lower()) + 13) % 26]

def rot13(cipertext):
    ciperwords = cipertext
    ciperwords = list(ciperwords)
    result = ""
    for word in ciperwords:
        if word != " ":
            result += rot13_letter(word)
        else:
            result += word
    return result
        
        
