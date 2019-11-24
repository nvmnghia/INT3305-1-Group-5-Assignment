import argparse
from enum import Enum
import math

from PIL import Image, ImageDraw, ImageColor


class Direction(Enum):
    HORIZONTAL = 'horizontal'
    VERTICAL   = 'vertical'
    DIAGONAL   = 'diagonal'


def get_default_width_height(direction):
    default_width_height = {}
    default_width_height[Direction.HORIZONTAL.value] = [1600, 200]
    default_width_height[Direction.VERTICAL.value]   = [200, 1600]
    default_width_height[Direction.DIAGONAL.value]   = [800, 800]

    return default_width_height[direction]


def get_width_height(direction, arg_width, arg_height):
    default_width, default_height = get_default_width_height(direction)

    arg_width = arg_width if arg_width is not None else default_width
    arg_height = arg_height if arg_height is not None else default_height

    return arg_width, arg_height


PERCEPTUAL_RED_STARTS_AT = 345


def gen_horizontal_gradient(width, height):
    img = Image.new('RGB', (width, height))
    img_draw = ImageDraw.Draw(img)

    # HSL has 360 hue
    hue_step = 360 / width
    for i in range(width):
        img_draw.line([(i, 0), (i, height)], width=1,
                       fill=ImageColor.getrgb(
                           f'hsv({int(hue_step * i)}, 100%, 100%)' if not PERCEPTUAL_RED else
                           f'hsv({int(hue_step * i + PERCEPTUAL_RED_STARTS_AT) % 360}, 100%, 100%)'
                        ))
    
    return img


def gen_vertical_gradient(width, height):
    return gen_horizontal_gradient(height, width).transpose(Image.ROTATE_90)


def gen_diagonal_gradient(width, height):
    img = Image.new('RGB', (width, height))
    img_draw = ImageDraw.Draw(img)

    num_of_line = width + height - 1    # Corner pixel
    hue_step = 360 / num_of_line

    for i in range(num_of_line):
        # Starting pixel
        start_pixel = {
            'x': 0 if i < height else i - height + 1,
            'y': i if i < height else height - 1
        }
        color = ImageColor.getrgb(
            f'hsv({int(hue_step * i)}, 100%, 100%)' if not PERCEPTUAL_RED else
            f'hsv({int(hue_step * i + PERCEPTUAL_RED_STARTS_AT) % 360}, 100%, 100%)'
        )

        num_of_drawn_pixel = 0
        while True:
            img_draw.point((start_pixel['x'] + num_of_drawn_pixel, start_pixel['y'] - num_of_drawn_pixel),
                           fill=color)
            num_of_drawn_pixel += 1

            if num_of_drawn_pixel > start_pixel['y']:
                break
    
    return img


parser = argparse.ArgumentParser('Generate gradient.')
parser.add_argument('-D', '--direction',
                    default=Direction.HORIZONTAL.value,
                    const=Direction.HORIZONTAL.value,
                    nargs='?',
                    choices=[d.value for d in Direction],
                    help='''Gradient direction: horizontal, vertical, diagonal.
                            Default is horizontal (default output 1600x200).
                            Vertical default outputs 200x1600.
                            Diagonal default outputs 800x800.''')
parser.add_argument('-W', '--width', metavar='W', type=int,
                    help='Output width')
parser.add_argument('-H', '--height', metavar='H', type=int,
                    help='Output height')
parser.add_argument('-O', '--output', metavar='O', type=str,
                    help='Output filename (default gradient.direction.png)')
parser.add_argument('-P', '--perceptual', dest='perceptual', action='store_true',
                    help='''Default starting hue of red is 0 degree.
                            This option moves it to 354 degree for perceptual "red".''')
args = parser.parse_args()

# Handle defaults
width, height = get_width_height(args.direction, args.width, args.height)

PERCEPTUAL_RED = True if args.perceptual else False
print(PERCEPTUAL_RED)

output = None
if args.direction == Direction.HORIZONTAL.value:
    output = gen_horizontal_gradient(width, height)
elif args.direction == Direction.VERTICAL.value:
    output = gen_vertical_gradient(width, height)
else:
    output = gen_diagonal_gradient(width, height)

output.save(args.output if args.output is not None 
            else 
                f'gradient.{args.direction}.perceptual.png' if PERCEPTUAL_RED
                else f'gradient.{args.direction}.png'
            )
