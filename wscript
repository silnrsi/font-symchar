#!/usr/bin/python3
# encoding: utf-8
# this is a smith configuration file

APPNAME = 'CharSym'
DESC_SHORT = "CharSym Fonts"

# build primary font
getufoinfo('source/CharSym-Regular.ufo')

designspace('source/CharSym.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            pdf = fret(params="-r -oi")
)

# build Keyman font
keymanpackage = package(appname = "CharSymK")

getufoinfo('source/CharSymK-Regular.ufo', keymanpackage)

designspace('source/CharSymK.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            pdf = fret(params="-r -oi"),
            package = keymanpackage
)

