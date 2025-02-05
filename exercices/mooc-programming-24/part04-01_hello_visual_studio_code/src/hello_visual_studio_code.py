# Write your solution here
while True:
    editor = input("Editor: ").lower()  # Convert input to lowercase
    
    if editor == "visual studio code":
        print("an excellent choice!")
        break  # Exit loop when the correct editor is entered
    elif editor in ["word", "notepad"]:
        print("awful")
    else:
        print("not good")