#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ledfonts.py
# Copyright (C) 2013 Pablo Castellano <pablo@anche.no>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from pprint import pprint


# c = content[0:2]  # ascii  Ñ = 0xD1, ñ = 0xF1 | hex(ord(u'Ñ'))
class LedFont:
    def __init__(self, filename=None):
        self.dict = {}
        if filename:
            self.load(filename)

    def load(self, filename):
        self.dict.clear()
        with open(filename, 'rb') as fp:
            content = fp.read()

        assert content[:2] in ('\x08\x08', '\x10\x09')
        content = content[2:]

        i = content.find('\x00\x00')
        while i != -1:
            c = content[0:1]
            self.dict[c] = content[2:i]
            content = content[9:]  # 2 char + 5 repr + 2 blank
            i = content.find('\x00\x00')

        print sorted(self.dict.keys())
        pprint(self.dict)

    def load2(self, filename):
        self.dict.clear()
        with open(filename, 'rb') as fp:
            content = fp.read()

        assert content[:2] in ('\x08\x08', '\x10\x09')
        content = content[2:]

        i = content.find('\x00\x00')
        while i != -1:
            c = content[0:1]
            self.dict[c] = content[2:i]
            content = content[i + 2:]
            i = content.find('\x00\x00')

        print sorted(self.dict.keys())
        pprint(self.dict)


if __name__ == '__main__':
    f = LedFont()
    print 'load1: Normal.fun'
    f.load('fuentes/Normal.fun')
    print 'load2: Normal.fun'
    f.load2('fuentes/Normal.fun')
    print '--------------------'
    print 'load1: Cursiva.fun'
    f.load('fuentes/Cursiva.fun')
    print 'load2: Cursiva.fun'
    f.load2('fuentes/Cursiva.fun')
    print '--------------------'
    print 'load1: Especial.fun'
    f.load('fuentes/Especial.fun')
    print 'load2: Especial.fun'
    f.load2('fuentes/Especial.fun')

#    print '--------------------'
#    print 'load1: twoline.fun'
#    f.load('fuentes/twoline.fun')
#    print 'load2: twoline.fun'
#    f.load2('fuentes/twoline.fun')
#    print '--------------------'
