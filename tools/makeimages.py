#!/usr/bin/env python
__doc__ = '''Create images for SymChar font docs '''
__url__ = 'https://github.com/silnrsi/font-symchar'
__copyright__ = 'Copyright (c) 2023 SIL International (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'Victor Gaultney'

# Switch to FormattedString()
# Test for max size emspace, refbox

# Requires drawBot library
from drawBot import *
import csv

# Specs
fname = "SymCharK"
fsize = 36
height = 48
width = 96
incsv = "../source/glyph_data.csv"
outfolder = "../documentation/images/"

def uconvert(u):
    usv = u
    unicode = chr(int(usv.replace('U+', ''), 16))
    return unicode

def make_image(left, char, righta, rightb):
    ch = uconvert(char)
    fl = "" if left == "" else uconvert(left)
    fra = "" if righta == "" else uconvert(righta)
    frb = "" if rightb == "" else uconvert(rightb)
    filename = outfolder + "img_" + char[2:6] + ".png"
    #frame = fl + ch + fra + frb

    frame = FormattedString()
    frame.font(fname)
    frame.fontSize(fsize)
    frame.align("center")
    frame.append (fl, fill=(0, 0, 0, 0.3))
    frame.append (ch, fill=(0, 0, 0, 1))
    frame.append (fra, fill=(0, 0, 0, 0.3))
    frame.append (frb, fill=(0, 0, 0, 0.3))

    newDrawing()
    size(width, height)
    stroke(None)
    fill(1, 1, 1, 1)
    rect(0, 0, width, height)
    #font(fname, fsize)
    #fill(0, 0, 0, 1)
    textBox(frame, (0, -2, width, height))
        
    endDrawing()

    saveImage(filename)

def main():
    # read csv
    with open(incsv, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        line_count = 0
        for row in csv_reader:
            if row["usv"] != "":
                make_image(row["frame_l"], row["usv"], row["frame_r1"], row["frame_r2"])
            line_count += 1
        print(f'Created {line_count} images')
    
if __name__ == "__main__": main()
