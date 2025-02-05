# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block

def line(length, character):
    if len(character) == 0:
        character = "*"
    else:
        character = character[0]
    print(character * length)

def shape(triangle_size, triangle_char, rectangle_height, rectangle_char):
    # Print the triangle
    for i in range(1, triangle_size + 1):
        line(i, triangle_char)
    
    # Print the rectangle
    for _ in range(rectangle_height):
        line(triangle_size, rectangle_char)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")
