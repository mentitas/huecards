from get_colors_from_image import save_to_numpy_array, alphabet
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import qrcode

def create_board(matrix, square_size, border):
    
    # Creo cuadricula de colores
    height, width, _ = matrix.shape

    # A3+ = 3720 x 5433
    board  = Image.new('RGB', (5433, 3720), "black")
    colors = Image.new('RGB', (32*square_size, 18*square_size), "black")

    # Armo los cuadrados de colores
    for j in range(16):
        for i in range(30):
            color  = tuple(matrix[i, j])
            square = Image.new('RGB', (square_size - border,  square_size - border), color)
            colors.paste(square, ((i+1) * square_size, (j+1) * square_size))

    draw = ImageDraw.Draw(colors)
    font = ImageFont.truetype(font='monospace.ttf', size=100)
    
    # Escribo las letras de la derecha
    for j in range(16):
        draw.text((30, (j+1)*square_size+30), '{: >2}'.format(alphabet[j]), fill="white", font=font)

    # Escribo los números de arriba
    for i in range(30):
        letter =  '{:0>2}'.format(i+1)
        draw.text(((i+1)*square_size+30, 30),  letter, fill="white", font=font)

    colors=colors.rotate(180)
    draw = ImageDraw.Draw(colors)

    # Escribo las letras de la izquierda
    for j in range(16):
        draw.text((30, (j+1)*square_size+30), '{: >2}'.format(alphabet[15-j]), fill="white", font=font)
    
    # Escribo los números de abajo
    for i in range(30):
        letter =  '{:0>2}'.format(30-i)
        draw.text(((i+1)*square_size+30, 30),  letter, fill="white", font=font)

    colors=colors.rotate(180)

    margin = (5433 - square_size*32)//2
    board.paste(colors, (margin,0))

    points = Image.new('RGB', (25*square_size, 4*square_size), "black")

    # Armo la primer fila de rectángulos grises
    gris = 50
    for i in range(25):
        square = Image.new('RGB', (square_size - border,     square_size*2-border), (gris, gris, gris))
        points.paste(square, (i * square_size, 0))
        gris = gris + 3

    # Armo la segunda fila de rectángulos grises
    gris = 50+50*3
    for i in range(25):
        square = Image.new('RGB', (square_size - border,     square_size*2-border), (gris, gris, gris))
        points.paste(square, (i * square_size, square_size*2))
        gris = gris - 3


    draw = ImageDraw.Draw(points)

    # Pongo los números de la primer fila
    for i in range(5, 26, 5):
        letter =  '{:0>2}'.format(i)
        draw.text(((i-1)*square_size+30, square_size+30),  letter, fill="white", font=font)
    
    # Pongo los números de la primer fila
    for i in range(0, 26, 5):
        letter =  '{:0>2}'.format(50-i)
        draw.text((i*square_size+30, square_size*3+ 30),  letter, fill="white", font=font)
    

    points = points.rotate(180)

    board.paste(points, (margin+square_size, square_size*18))


    board = board.rotate(180)

    qr_image = qrcode.make('https://mentitas.github.io/huecards/')
    board.paste(qr_image, (90,90))
    
    draw = ImageDraw.Draw(board)

    titulo = r"""Hues
 and
Cues"""
    descripcion_qr = r"""¡Accedé al QR para
ver qué color te
toca describir!"""
    draw.text((90,670),"Este tablero está 100% hecho en Python :-]", fill="white", font=ImageFont.truetype(font='monospace.ttf', size=30))
    draw.text((90,490),descripcion_qr, fill="white", font=ImageFont.truetype(font='monospace.ttf', size=50))
    draw.text((620,50),titulo, fill="white", font=ImageFont.truetype(font='monospace.ttf', size=200))

    board = board.rotate(180)
    board.show()
    board.save("board.png")


matrix = save_to_numpy_array()
create_board(matrix, 165, 15)