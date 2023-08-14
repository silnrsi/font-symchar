#!/usr/bin/python3
# encoding: utf-8
# this is a smith configuration file

APPNAME = 'CharSym'
DESC_SHORT = "CharSym Fonts"
DEBPKG = 'fonts-sil-charsym'

getufoinfo('source/CharSym-Regular.ufo')

fontfamily=APPNAME

designspace('source/' + fontfamily + '.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            pdf = fret(params="-r -oi"),
)
