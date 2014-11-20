#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from helper import *
import sys

def find_first_position (string, func):
    for i, c in enumerate(string):
        if func(c): return i
    return -1

def myanmar_phonemic_iter(string):
    startpos = 0
    while startpos < len(string):
        curstr = string[startpos:]

        if not ismyanmar(curstr[0]):
            yield curstr[0]
            startpos += 1
            continue

        # first cons position
        fcp = find_first_position(curstr, ismyconsonant)
        if fcp > 0:
            # if the string do not start with consonant
            endpos = 1
            while ismyanmar(curstr[endpos]) and endpos < fcp: endpos += 1
            startpos = startpos + endpos
            yield curstr[:endpos]
            continue

        endpos = 1
        while endpos < len(curstr) and ismymark(curstr[endpos]): endpos += 1
        if endpos < len(curstr) and ismyconsonant(curstr[endpos]):
            if endpos + 1 < len(curstr) and curstr[endpos+1] == SIGN_ASAT:
                endpos += 2
                while endpos < len(curstr) and ismytone(curstr[endpos]): endpos += 1
                yield curstr[:endpos]
                # skip kinzi virama
                if endpos < len(curstr) and curstr[endpos] == SIGN_VIRAMA: endpos += 1
                startpos = startpos + endpos
                continue
            if endpos + 2 < len(curstr) and curstr[endpos+1] == SIGN_DOT_BELOW and \
               curstr[endpos+2] == SIGN_ASAT:
                endpos += 3
                while endpos < len(curstr) and ismytone(curstr[endpos]): endpos += 1
                yield curstr[:endpos]
                startpos = startpos + endpos
                continue

            if endpos + 1 < len(curstr) and curstr[endpos+1] == SIGN_VIRAMA:
                endpos += 2
                syll = curstr[:endpos-1] + SIGN_ASAT # replace virama with asat
                #syll[-1] = SIGN_ASAT
                yield syll
                startpos = startpos + endpos
                continue

        yield curstr[:endpos]
        startpos = startpos + endpos
        continue

    raise StopIteration


class Romanizer():
    data = None # subclass needs to override this

    @staticmethod
    def romanize (cls_type, string):
        if not issubclass(cls_type, Romanizer):
            raise TypeError("cls type must be a subclass of Romanizer.")
        return cls_type.romanize_(string)

    @classmethod
    def romanize_(cls, string):
        romans = []
        maxkeylen = max(len(k) for k in cls.data.keys())
        for phoneme in myanmar_phonemic_iter(string):
            romanstr = ""
            curpos = 0
            print(phoneme)
            while curpos < len(phoneme):
                lookuplen = len(phoneme)
                while lookuplen > 0:
                    lookupstr = phoneme[curpos:lookuplen]
                    #print('\t'+ str(lookuplen)+ phoneme[curpos:lookuplen]+ romanstr)
                    if lookupstr in cls.data:
                        romanstr += cls.data[lookupstr]
                        curpos += (lookuplen - curpos)
                        break
                    else:
                        lookuplen -= 1
                else:
                    #sys.stderr.write("Unable to romanize " + phoneme[curpos] + '\n')
                    romanstr += phoneme[curpos]
                    curpos += 1
            romans.append(romanstr)

        return cls.join_(romans)

    @classmethod
    def join_(cls, romans):
        return "".join(romans)

import bgn_pcgn
class BGN_PCGN(Romanizer):
    data = bgn_pcgn.data
    vowels = 'aeèioôu'

    @classmethod
    def join_(cls, romans):
        new_romans = []
        for i, roman in enumerate(romans):
            roman = cls.handle_letter_a (roman)
            roman = cls.add_vowel_a_if_necessary(roman)

            if roman.startswith('k') and i > 0:
                if new_romans[i-1][-1] in 'aeioun' or new_romans[i-1].endswith('ng'):
                    # change ka to ga after vowel sound
                    roman = 'g' + roman[1:]

            if roman.startswith('s') and i > 0:
                if new_romans[i-1][-1] in 'aeioun' or new_romans[i-1].endswith('ng'):
                    # change sa to za after vowel sound
                    roman = 'z' + roman[1:]

            if roman.startswith('p') and i > 0:
                if new_romans[i-1][-1] in 'aeioun' or new_romans[i-1].endswith('ng'):
                    # change pa to ba after vowel sound
                    roman = 'b' + roman[1:]

            if roman.startswith('t') and not roman.startswith('th') and i > 0:
                if new_romans[i-1][-1] in 'aeioun' or new_romans[i-1].endswith('ng'):
                    # change ta to da after vowel sound
                    roman = 'd' + roman[1:]

            if roman[0] in cls.vowels and i > 0 and not new_romans[i-1][-1].isspace():
                # add hyphen if started with a vowel
                roman = '-' + roman

            if roman[0] in 'gy' and i > 0 and new_romans[i-1][-1] == 'n':
                # to differetiate ng & ny
                roman = '-' + roman

            if roman[0] == 'h' and i > 0 and new_romans[i-1][-1] == 't':
                roman = '-' + roman

            new_romans.append(roman)

        #print(new_romans)
        return "".join(new_romans)

    @classmethod
    def handle_letter_a(cls, roman):
        if roman.startswith ('a') and cls.has_vowel(roman[1:]):
            return roman[1:]
        return roman

    @classmethod
    def has_vowel(cls, roman):
        for v in cls.vowels:
            #print type(v), type(roman)
            if roman.find(v) != -1:
                return True
        return False

    @classmethod
    def add_vowel_a_if_necessary(cls, roman):
        if cls.has_vowel(roman):
            return roman
        else:
            return roman + 'a'

if __name__ == "__main__":
    romanizer = BGN_PCGN_Romainzer()
