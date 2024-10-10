from PIL import Image
import csv
import json

img = Image.open('hue_cut.jpg')
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

#save_to_csv()
save_to_json()