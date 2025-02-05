# Write your solution here
# You can test your function by calling it within the following block

def spruce(size):
    print("a spruce!")
    for i in range(size):
        spaces = size - i - 1
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)
    print(" " * (size - 1) + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)
    print()
    spruce(5)