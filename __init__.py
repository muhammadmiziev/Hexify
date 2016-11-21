#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


class Hexify():
    def __init__(self):
        pass

    def toHexify(self, input):
        self.input = input.decode('utf-8');

        lenhex = len(self.input)

        lenfactor = 4;
        lencount = lenfactor

        rowsfactor = 6*lenfactor
        rows = rowsfactor;

        result = ''''''

        for i in range(1):
            for i in range(lenhex):
                if(i >= lencount):
                    lencount += lenfactor;
                    result += "\t"
                if(i >= rows):
                    rows += rowsfactor;
                    result += "\n"
                result += (self.input[i])
        return result

    def toUnhexify(self, str):
        out = re.sub(r'\n|\t', '', str.decode('utf-8'))
        return out
