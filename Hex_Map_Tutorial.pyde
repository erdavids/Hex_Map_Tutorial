# Hexagon Map Tutorial - Part One

w, h = 1000, 1000

hex_size = 10

grid_x_pixels = .9 * w
grid_y_pixels = .9 * h

sep_x = 3 * hex_size
sep_y = .86 * hex_size

grid_x = int(grid_x_pixels / sep_x) + 1
grid_y = int(grid_y_pixels / sep_y) + 1

def draw_hexagon(x, y, side):
    beginShape()
    vertex((x + side * sin(PI/2), y + side * cos(PI/2)))
    vertex((x + side * sin(PI/6), y + side * cos(PI/6)))
    vertex((x + side * sin(11 * PI/6), y + side * cos(11 * PI/6)))
    vertex((x + side * sin(3 * PI/2), y + side * cos(3 * PI/2)))
    vertex((x + side * sin(7 * PI/6), y + side * cos(7 * PI/6)))
    vertex((x + side * sin(5 * PI/6), y + side * cos(5 * PI/6)))
    endShape(CLOSE)

def setup():
    # Create the Canvas
    size(w, h)
    background(255)
    
    # Higher resolution
    pixelDensity(2)
    
    # Shape Details
    strokeWeight(2)
    stroke(0)
    noFill()
    
    
    # Draw the Grid
    current_x = w/2.0 - grid_x_pixels/2.0
    current_y = h/2.0 - grid_y_pixels/2.0
    for i in range(grid_y):
        if (i % 2 == 0):
            current_x += 1.5 * hex_size
        for j in range(grid_x):

            draw_hexagon(current_x, current_y, hex_size)
            
            current_x += sep_x
        current_x = w/2.0 - grid_x_pixels/2.0
        current_y += sep_y
