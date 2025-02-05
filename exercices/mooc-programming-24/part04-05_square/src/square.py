# Copy here code of line function from previous exercise

def line(length, character):
    if len(character) == 0:
        character = "*"
    else:
        character = character[0]
    print(character * length)

def square(size, character):
    for _ in range(size):
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "*")
    print()
    square(3, "o")