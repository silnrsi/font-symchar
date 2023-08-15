#!/usr/bin/python3
# encoding: utf-8
# this is a smith configuration file

DOCDIR = ["documentation", "web"]

APPNAME = 'SymChar'
DESC_SHORT = "SymChar Fonts"

# build primary font
getufoinfo('source/SymChar-Regular.ufo')

designspace('source/SymChar.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            pdf = fret(params="-r -oi"),
            woff = woff('web/${DS:FILENAME_BASE}',
                metadata = f'../source/SymChar-WOFF-metadata.xml')
)

# build Keyman font
keymanpackage = package(appname = "SymCharK", docdir = DOCDIR)

getufoinfo('source/SymCharK-Regular.ufo', keymanpackage)

designspace('source/SymCharK.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            pdf = fret(params="-r -oi"),
            woff = woff('web/${DS:FILENAME_BASE}',
                metadata = f'../source/SymCharK-WOFF-metadata.xml'),
            package = keymanpackage
)

