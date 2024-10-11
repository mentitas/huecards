from PIL import Image
import csv
import json
import numpy as np

img = Image.open('original_board.jpg')
pixels = img.load() 
width, height = img.size

def save_to_csv():
    with open('all_the_colors.csv', 'w', newline='') as csvfile:
    
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)    
        for y in range(18, height, 37):
            row = []
            for x in range(18, width, 37):
                r, g, b = pixels[x, y]
        
                row.append(f"{r:02x}{g:02x}{b:02x}")
            writer.writerow(row)

def save_to_json():

    dictionary = {}
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"];

    index = 0
    for y in range(18, height, 37):
        row = []
        for x in range(18, width, 37):
            r, g, b = pixels[x, y]
            row.append(f"#{r:02x}{g:02x}{b:02x}")
    
        dictionary[alphabet[index]] = row
        index = index+1

    f = open("../colors.json", "w")
    f.write("colors = " + json.dumps(dictionary))
    f.close()


def save_to_numpy_array():

    color_matrix = np.ones((30, 16, 3), dtype=np.uint8)

    for y in range(16):
        for x in range(30):
            pixel_x = 18 + 37*x
            pixel_y = 18 + 37*y

            r, g, b = pixels[pixel_x, pixel_y]
            
            color_matrix[x,y,0] = r
            color_matrix[x,y,1] = g
            color_matrix[x,y,2] = b

    return color_matrix


def create_board(square_size, matrix):
    
    height, width, _ = matrix.shape
    
    board_image = Image.new('RGB', (width * square_size, height * square_size))
    
    for i in range(height):
        for j in range(width):
            color = tuple(matrix[i, j])
            square       = Image.new('RGB', (square_size-7, square_size-7), color)
            black_square = Image.new('RGB', (square_size,   square_size), "black")
            board_image.paste(black_square, (j * square_size, i * square_size))
            board_image.paste(square, (j * square_size, i * square_size))
    
    board_image.save('board.png')
    board_image.show()

matrix = save_to_numpy_array()
create_board(100, matrix)