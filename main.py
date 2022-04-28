from PIL import Image, ImageDraw
import cv2
import os
import sys

grid_height = 1500
grid_width = 2000
puzzle_pieces = 48

grid_height = int(sys.argv[2])
grid_width = int(sys.argv[1])
puzzle_pieces = int(sys.argv[3])

brut_height_list = []
brut_width_list = []
puzzle_count = 0
puzzle_size = 0
puzzle_rows = 0
puzzle_cols = 0


def testSquare(size, width):
    square_size = size
    square_count = 0
    square_index = 0
    width_index = 0
    while 1:
        if width_index == width:
            return square_size
        if width_index >= width + 1:
            return False
        else:
            square_count = square_count + 1
            width_index = (square_size * square_count)

def bruteforce(muhlist, width):
    inc = 0
    while 1:
        x = range(1, width, 1 + inc)
        for n in x:
            result = testSquare(n, width)
            if result:
                muhlist.append(result)
        if inc >= width:
            return False
        inc = inc + 1

def getJigsawCount(size, height, width):
    height_count = height / size
    width_count = width / size
    total_count = height_count * width_count
    return [total_count, size, height_count, width_count]

def main():
    bruteforce(brut_width_list, grid_width)
    bruteforce(brut_height_list, grid_height)
    res = set(brut_height_list).intersection(brut_width_list)

    results_list = []
    for piece_size in res:
        jig = getJigsawCount(piece_size, grid_height, grid_width)
        results_list.append(jig)


    closest_list = min(results_list, key=lambda x:abs(x[0]-puzzle_pieces))
    print(closest_list)

    image = Image.new("RGBA", (grid_width, grid_height))
    draw = ImageDraw.Draw(image)


    x = range(0, grid_width, closest_list[1])
    for n in x:
        draw.line([(n, 0), (n, grid_height)], fill=(255,0,255), width=1, joint=None)
    x = range(0, grid_height, closest_list[1])
    for n in x:
        draw.line([(0, n), (grid_width, n)], fill=(255,0,255), width=1, joint=None)


    image.save(sys.path[0] + "\\grid.png", "PNG")

if __name__ == '__main__':
    main()