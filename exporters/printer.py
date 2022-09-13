#
# Simple exporter for fontedit
#
# Exports as the font generator ROM for a 7 head dot matrix printer
#

# export function, name is unimportant but must be in the exporters
# dictionary below.  Must take a font object and filename as arguments.
def export(font, filename):

    # useful properties of the font object:
    # font.cols - the number of columns per character (i.e. width in px)
    # font.rows - the number of rows per character (i.e. height in px)
    # font.chars - total number of characters in the font
    # font.get_character(i) - get character number i (where 0<=i<font.chars)
    #                         returns a list of rows of integers
    #                         1 represents foreground in the editor,
    #                         0 represents background
    if font.cols != 5:
        # returning a string will popup an error message in the editor
        return "Can only handle fonts of width 5"
    if font.rows != 7:
        # returning a string will popup an error message in the editor
        return "Can only handle fonts of height 7"

    # open a file for writing
    with open(filename, "wb") as fw:
        # leading blanks (characters 0-32 not supported)
        for i in range(33):
            fw.write(b'\xff')

        # iterate over columns
        for k in range(font.cols):
            # iterate over all characters
            for i in range(33, font.chars):
                # fetch the array of pixels
                c = font.get_character(i)
                # iterate over the rows
                b = 0
                for j in range(font.rows):
                    # make a single byte bitmask of one column
                    b |= c[j][k] << j
                    # write the byte
                fw.write(b.to_bytes(1, 'big'))

        # trailing blanks
        for i in range(676):
            fw.write(b'\xff')

    # return zero to indicate that we were successful
    return 0


# the exporters dict is where the program finds the importer from
# needs name, desc and func parts.
exporters = {"name": "Printer",
             "desc": "Formatted for 7 head dot matrix printer",
             "func": export}
