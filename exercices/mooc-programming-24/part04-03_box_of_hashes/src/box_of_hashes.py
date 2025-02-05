# Copy here code of line function from previous exercise

def line(length, character):
    if len(character) == 0:
        character = "*"
    else:
        character = character[0]
    print(character * length)

def box_of_hashes(height):
    for _ in range(height):
        line(10, "#")

