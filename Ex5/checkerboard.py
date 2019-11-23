import sys
import argparse

from PIL import Image, ImageDraw


def draw(img_draw, column, row, ssize):
    '''
    Draw a black square at the given column and row.
    Column and row number (origin (1, 1) at lower left)
    will be converted into PIL coordinate numbers
    (2 coordinates for bound, origin (0,0) at upper left).
    '''

    x0 = ssize * (column - 1)
    y0 = img.height - ssize * row

    x1 = x0 + ssize - 1
    y1 = y0 + ssize - 1

    img_draw.rectangle([(x0, y0), (x1, y1)], fill=(0, 0, 0))


parser = argparse.ArgumentParser(description='Generate checkerboard pattern.')
parser.add_argument('-c', '--column', metavar='C',
                    type=int, default=8,
                    help='Number of column (default 8)')
parser.add_argument('-r', '--row', metavar='R',
                    type=int, default=8,
                    help='Number of row (default 8)')
parser.add_argument('-s', '--ssize', metavar='S',
                    type=int, default=200,
                    help='Size of each square (default 200 px)')
parser.add_argument('output', metavar='O',
                    type=str, nargs='?', default='checkerboard.png',
                    help='Output filename (default output.png)')
args = parser.parse_args()

ssize = args.ssize
img_width = args.column * ssize
img_height = args.row * ssize

# White canvas
img = Image.new('RGB', (img_width, img_height), color='white')

img_draw = ImageDraw.Draw(img)

# Draw black square from the lower left corner
# The lower left square must be black
for i in range(1, args.row + 1):
    for j in range(i % 2, args.column + 1, 2):
        draw(img_draw, j, i, ssize)

img.save(args.output)
