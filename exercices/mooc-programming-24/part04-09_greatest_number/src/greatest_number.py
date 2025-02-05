# Write your solution here
# You can test your function by calling it within the following block

def greatest_number(a, b, c):
    return max(a, b, c)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)  # 8
    print(greatest_number(3, 4, 1))  # 4
    print(greatest_number(99, -4, 7))  # 99
    print(greatest_number(0, 0, 0))  # 0