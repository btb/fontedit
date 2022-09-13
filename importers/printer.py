
def doimport(font, filename):
  # useful properties of the font object:
  # font.cols - the number of columns per character (i.e. width in px)
  # font.rows - the number of rows per character (i.e. height in px)
  # font.chars - total number of characters in the font
  # font.get_character(i) - get character number i (where 0<=i<font.chars)
  #                         returns a list of rows of integers
  #                         1 represents foreground in the editor,
  #                         0 represents background

  font.__init__(7, 5, 96)
  font.fg = {'r': 0, 'g': 0, 'b': 0}
  font.bg = {'r': 65535, 'g': 65535, 'b': 65535}

  # open a file for reading
  with open(filename, "rb") as file:
    # iterate over all characters
    for i in range(0x21, font.chars):
      cols = b""
      file.seek(i)
      cols += file.read(1)
      file.seek(62, 1)
      cols += file.read(1)
      file.seek(62, 1)
      cols += file.read(1)
      file.seek(62, 1)
      cols += file.read(1)
      file.seek(62, 1)
      cols += file.read(1)

      pixels = []
      for row in range(font.rows):
        pixels.append([])
      for col in range(font.cols):
        for row in range(font.rows):
          pixels[row].append((cols[col] >> row) & 1)

      font.set_character(i, pixels)
  font.changed = True

  return 0


# the exporters dict is where the program finds the importer from
# needs name, desc and func parts.
importers = {"name": "Dot Matrix",
             "desc": "Formatted for 7 head dot matrix",
             "func": doimport}
