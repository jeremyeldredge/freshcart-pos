# scan item and subtotal funcitons

cart = []
def scan_item():
    add_more = "yes"
    while add_more == "yes":
        description = input("Item description: ")
        price = float(input("Item price: "))
        quantity = int(input("Quantity: "))
        cart.append({'description' : description, 'price' : price, 'quantity' : quantity})
        add_more = input("Would you like to scan another item? (yes/no)").lower()
    return cart

def calculate_subtotal():
    subtotal = 0
    for item in cart:
        subtotal += item['price'] * item['quantity']
    return subtotal