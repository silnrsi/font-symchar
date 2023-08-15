#!/usr/bin/env python
__doc__ = '''Create markdown encoding table for SymChar font docs '''
__url__ = 'https://github.com/silnrsi/font-symchar'
__copyright__ = 'Copyright (c) 2023 SIL International (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'Victor Gaultney'

import csv

incsv = "../source/glyph_data.csv"
outfile = "../documentation/encoding.md"
header = """# Encoded Symbols

These are the encoded characters in the SymChar fonts. The symbols representing common "invisible" characters are shown in context. The Fonts column indicates which of the SymChar fonts contain that symbol - SymChar (S), SymCharK (K).

"""

def main():
    tablehead = "Image | USV | Fonts | Description | Represents\n"
    tablediv  = "----- | --- | ----- | ----------- | ----------\n"
    tablerows = ""
    # read csv
    with open(incsv, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            if row["usv"] != "" and row["in_docs"] == "D":
                fonts = ""
                if row["in_g"] == "Y": fonts += "S"
                if row["in_k"] == "Y": fonts += "K"
                newrow = "![](images/img_" + row["usv"][2:6] + ".png)" + " | " + row["usv"] + " | " + fonts + " | " + row["doc_name"] + " | " + row["doc_uni"] + "\n"
                tablerows += newrow

    table = tablehead + tablediv + tablerows

    output = open(outfile,'w')
    output.write(header)
    output.write(table)
    output.close()
    
if __name__ == "__main__": main()
