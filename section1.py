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
        subtotal += item('price')
    return subtotal

#member2

def check_stock(item_name, inventory):
    item = inventory.get(item_name)
    if item:
        return item["stock"]
    else:
        return -1  # Item not found
def update_stock(item_name, inventory):
    item = inventory.get(item_name)
    if item and item["stock"] > 0:
        item["stock"] -= 1
        return True
    else:
        return False  # Item not found or out of stock

        subtotal += item['price'] * item['quantity']
    return subtotal
