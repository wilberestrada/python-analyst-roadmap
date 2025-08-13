def build_inventoy():
    print("=== Inventory Builder ===")
    print("To exit, type STOP\n")

    inventory = {}

    while True:
        product_name = input("Enter product name: ").strip()
        if not product_name:
            print("Product name cannot be empty.\n")
            continue

        # exit condition (case-insensitive)
        if product_name.upper()  == "STOP":
            break

        # quantity input with per-entry validation
        while True:
            qty_str = input(f"Enter quantity for {product_name}: ").strip()
            try:
                qty = int(qty_str)
                if qty < 0:
                    print("Quantity must be >= 0. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
    
        # accumulate quantities for repeated products
        key = product_name.lower()
        inventory[key] = inventory.get(key, 0) + qty

    return inventory

def print_summary(inventory: dict):
    print("\n---Inventory Summary ---")
    print(f"Distinct products: {len(inventory)}")
    print(f"Total items in stock: {sum(inventory.values())}")

    zero_stock = sorted([k for k, v in inventory.items() if v == 0])
    if zero_stock:
        print("Products with zero stock:", ", ".join(sorted(zero_stock)))
    else:
        print("Products with zero stock: All in stock")

if __name__ == "__main__":
    inv = build_inventoy()
    print_summary(inv)
