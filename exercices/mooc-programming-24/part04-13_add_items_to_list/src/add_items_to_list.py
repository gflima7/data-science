num_items = int(input("How many items: "))

items = []
for i in range(num_items):
    item = int(input(f"Item {i + 1}: "))
    items.append(item)

print(items)