from get_colors_from_image import save_to_numpy_array, alphabet
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import qrcode

def draw_gray_rectangles(image, y, base_size, border, colors):

    for index, color in enumerate(colors):
        rectangle = Image.new('RGB', (base_size - border, base_size*2-border), (color,color,color))
        image.paste(rectangle, (index * base_size, y))

def write_numbers(image, y, spacing, numbers):
    
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='monospace.ttf', size=100)

    for index, number in enumerate(numbers):
        if number != "":
            label = '{:0>2}'.format(number)
            draw.text((index*spacing+30, y), label, fill="white", font=font)
    
def write_axis(image, spacing, x_axis, y_axis):

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='monospace.ttf', size=100)
    
    # Escribo las letras de la derecha
    for index, elem in enumerate(y_axis):
        label = '{: >2}'.format(elem)
        pos = (30, (index+1)*spacing+30)
        draw.text(pos, label, fill="white", font=font)

    # Escribo los números de arriba
    for index, elem in enumerate(x_axis):
        label = '{:0>2}'.format(elem)
        pos = ((index+1)*spacing+30, 30)
        draw.text(pos, label, fill="white", font=font)

def create_board(matrix, square_size, border):
    
    # Creo cuadricula de colores
    height, width, _ = matrix.shape

    # A3  = 3508 x 4960
    # A3+ = 3720 x 5433
    board  = Image.new('RGB', (4960, 3508), "black")
    colors = Image.new('RGB', (32*square_size, 18*square_size), "black")

    # Armo los cuadrados de colores
    for y in range(width):
        for x in range(height):
            color  = tuple(matrix[x, y])
            square = Image.new('RGB', (square_size - border,  square_size - border), color)
            colors.paste(square, ((x+1) * square_size, (y+1) * square_size))
    
    write_axis(colors, square_size, range(1,31), alphabet)
    colors=colors.rotate(180)
    write_axis(colors, square_size, range(30,0,-1), alphabet[::-1])
    colors=colors.rotate(180)

    margin = (4960 - square_size*32)//2
    board.paste(colors, (margin,margin))

    points = Image.new('RGB', (25*square_size, 4*square_size), "black")

    draw_gray_rectangles(points,             0, square_size, border, range(50,126,3))
    draw_gray_rectangles(points, square_size*2, square_size, border, range(200,125,-3))

    draw = ImageDraw.Draw(points)
    font = ImageFont.truetype(font='monospace.ttf', size=100)

    write_numbers(points,   square_size+30, square_size, [ i if i % 5 == 0 else "" for i in range(1,26)])
    write_numbers(points, 3*square_size+30, square_size, [ i if i % 5 == 0 else "" for i in range(50,25,-1)])

    points = points.rotate(180)

    board.paste(points, (margin+square_size, 3508-margin-square_size*4))

    board = board.rotate(180)

    qr_image = qrcode.make('https://mentitas.github.io/huecards/')
    board.paste(qr_image, (90,90))
    
    draw = ImageDraw.Draw(board)

    titulo = r"""Hues
 and
Cues"""
    descripcion_qr = r"""¡Accedé al QR
para ver qué color
te toca describir!"""
    comentario = r"""Este tablero fue programado 100%
en Python por Flor Rosenzuaig :-]"""


    draw.text((90,490),descripcion_qr, fill="white", font=ImageFont.truetype(font='monospace.ttf', size=70))
    draw.text((575,50),titulo, fill="white", font=ImageFont.truetype(font='monospace.ttf', size=150))

    board = board.rotate(90, expand=True)
    draw = ImageDraw.Draw(board)

    draw.text((90,145),comentario, fill="white", font=ImageFont.truetype(font='monospace.ttf', size=35))
    
    board = board.rotate(90, expand=True)
    board.show()
    board.save("board.png")


matrix = save_to_numpy_array()
create_board(matrix, 150, 15)