def hello(): 
    print("Hello! Welcome to our program.")

def pack(item1, item2, item3):
    return [item1, item2, item3]

def eat_lunch(food_list):
    if not food_list:
        print("lunchbox empty")
    else:
        print("First I eat", food_list[0])
    for item in food_list[1:]:
        print("Next I eat", item)

hello()
print("Packed items:", pack("Sandwich", "Apple", "Chips"))
eat_lunch(["Salad", "Soup", "Bread"])
