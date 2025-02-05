# Copy here code of line function from previous exercise


def line(length, character):
    if len(character) == 0:
        character = "*"
    else:
        character = character[0]
    print(character * length)

def square_of_hashes(size):
    for _ in range(size):
        line(size, "#")

if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)