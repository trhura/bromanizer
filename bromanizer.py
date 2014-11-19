#! /usr/bin/env python
# -*- coding: utf-8 -*-

from helper import *

def find_first_position (string, func):
    for i, c in enumerate(string):
        if func(c): return i
    return -1

def my_phonemic_iter(string):
    if not isinstance(string, unicode):
        string = unicode(string, "utf-8")

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
                yield curstr[:endpos]
                startpos = startpos + endpos
                continue

            if endpos + 1 < len(curstr) and curstr[endpos+1] == SIGN_VIRAMA:
                endpos += 2
                syll = curstr[:endpos]
                syll[-1] = SIGN_ASAT # replace virama with asat
                yield syll
                startpos = startpos + endpos
                continue

        yield curstr[:endpos]
        startpos = startpos + endpos
        continue

    raise StopIteration

if __name__ == "__main__":
    main()
