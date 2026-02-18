# Simple Hotel Bill Generator using Python

def hotel_bill():
    print("\n==========Sunflower HOTEL BILL ==========")
    print("Hotel Name : Sunshine Hotel")

    name = input("Enter Customer Name: ")
    date = input("Enter Date (dd-mm-yyyy): ")

    print("\n------ MENU ------")
    print("1. Tea        - 10")
    print("2. Coffee     - 40")
    print("3. Sandwich   - 60")
    print("4. Burger     - 80")
    print("5. Pizza      - 120")

    total = 0
    bill_items = []

    while True:
        choice = int(input("\nEnter item number (0 to finish): "))

        if choice == 0:
            break

        qty = int(input("Enter quantity: "))

        if choice == 1:
            item = "Tea"
            price = 10 * qty
        elif choice == 2:
            item = "Coffee"
            price = 40 * qty
        elif choice == 3:
            item = "Sandwich"
            price = 60 * qty
        elif choice == 4:
            item = "Burger"
            price = 80 * qty
        elif choice == 5:
            item = "Pizza"
            price = 120 * qty
        else:
            print("Invalid choice")
            continue

        bill_items.append((item, qty, price))
        total += price

    print("\n========== FINAL BILL ==========")
    print("Customer :", name)
    print("Date     :", date)
    print("--------------------------------")
    print("Item        Qty   Price")
    print("--------------------------------")

    for item, qty, price in bill_items:
        print(f"{item:<12} {qty:<5} {price}")

    print("--------------------------------")
    print("Total Amount =", total)
    print("Thank You! Visit Again")
    print("================================")


# Function Call
hotel_bill()

