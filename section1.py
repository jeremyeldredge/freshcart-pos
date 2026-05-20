INVENTORY = {
    "apple":   {"price": 1.25, "stock": 50},
    "bread":   {"price": 3.49, "stock": 30},
    "milk":    {"price": 4.99, "stock": 20},
    "cheese":  {"price": 6.75, "stock": 15},
    "chips":   {"price": 3.99, "stock": 40},
    "soda":    {"price": 1.99, "stock": 60},
    "eggs":    {"price": 5.49, "stock": 25},
    "chicken": {"price": 8.99, "stock": 10},
}

MEMBERS = {
    "M001": {"name": "Sarah Johnson",  "discount": 0.10},
    "M002": {"name": "Mike Chen",      "discount": 0.15},
    "M003": {"name": "Emma Davis",     "discount": 0.05},
}




# scan item and subtotal funcitons
def scan_item():
    """
    Inputs: None
    Processes: Scan all items and add them to a cart.
    Outputs: A list with dictionaries of items containing their description, price, and quantity."""
    cart = []
    add_more = "yes"
    while add_more == "yes":
        description = input("Item description: ")
        # Need input validation for price and quantity
        price = float(input("Item price: "))
        quantity = int(input("Quantity: "))
        cart.append({'description' : description, 'price' : price, 'quantity' : quantity})
        add_more = input("Would you like to scan another item? (yes/no)").lower()
    return cart

def calculate_subtotal():
    for item in cart:
        subtotal += item('price')
    return subtotal


#### Receipt functions

def calculate_tax(amount, tax_rate=0.0825):
    """Calculate tax for a given amount."""
    return amount * tax_rate

def print_receipt(quantities, items, subtotal, membership, discount, total):
    """Print a formatted receipt."""
    print("\n" + "="*30)
    print("FRESHCART RECEIPT")
    print("="*30)
    for qty, item in zip(quantities, items):
        print(f"{qty} x {item['name']} @ ${item['price']:.2f}")
    print("-"*30)
    print(f"Subtotal: ${subtotal:.2f}")
    if membership:
        print(f"Membership Discount: -${discount:.2f}")
    print(f"Tax: ${calculate_tax(subtotal - discount):.2f}")
    print(f"Total (incl. tax): ${total:.2f}")
    print("="*30)
    
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

def is_member(member_id):
    """Check if the provided member ID is valid."""
    return member_id in MEMBERS

def apply_member_discount(subtotal, member_id):
    """Apply member discount to the subtotal."""
    if is_member(member_id):
        discount_rate = MEMBERS[member_id]["discount"]
        return subtotal * discount_rate
    return 0.0



# Run whole system
# User walks up to register
# What happens

# 1. Scan items
cart = scan_item()
# 2. Calculate subtotal
subtotal = calculate_subtotal(cart)

# 3. Member discount
member_id = input("Enter your member ID (or press Enter to skip): ")
if member_id and is_member(member_id):
    print(f"Welcome back, {MEMBERS[member_id]['name']}! You get a {MEMBERS[member_id]['discount']*100:.0f}% discount.")
    discount = apply_member_discount(subtotal, member_id)
