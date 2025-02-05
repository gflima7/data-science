
def line(length, character):
        if len(character) == 0:
            character = "*"
        else:
            character = character[0]
        print(character * length)

if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "")