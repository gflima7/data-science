# Copy here code of line function from previous exercise

def line(length, character):
    if len(character) == 0:
        character = "*"
    else:
        character = character[0]
    print(character * length)

def triangle(size):
    for i in range(1, size + 1):
        line(i, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)