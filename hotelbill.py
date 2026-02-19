# # Simple Hotel Bill Generator using Python

# def hotel_bill():
#     print("\n==========Sunflower HOTEL BILL ==========")
#     print("Hotel Name : Sunshine Hotel")

#     name = input("Enter Customer Name: ")
#     date = input("Enter Date (dd-mm-yyyy): ")

#     print("\n------ MENU ------")
#     print("1. Tea        - 10")
#     print("2. Coffee     - 40")
#     print("3. Sandwich   - 60")
#     print("4. Burger     - 80")
#     print("5. Pizza      - 120")

#     total = 0
#     bill_items = []

#     while True:
#         choice = int(input("\nEnter item number (0 to finish): "))

#         if choice == 0:
#             break

#         qty = int(input("Enter quantity: "))

#         if choice == 1:
#             item = "Tea"
#             price = 10 * qty
#         elif choice == 2:
#             item = "Coffee"
#             price = 40 * qty
#         elif choice == 3:
#             item = "Sandwich"
#             price = 60 * qty
#         elif choice == 4:
#             item = "Burger"
#             price = 80 * qty
#         elif choice == 5:
#             item = "Pizza"
#             price = 120 * qty
#         else:
#             print("Invalid choice")
#             continue

#         bill_items.append((item, qty, price))
#         total += price

#     print("\n========== FINAL BILL ==========")
#     print("Customer :", name)
#     print("Date     :", date)
#     print("--------------------------------")
#     print("Item        Qty   Price")
#     print("--------------------------------")

#     for item, qty, price in bill_items:
#         print(f"{item:<12} {qty:<5} {price}")

#     print("--------------------------------")
#     print("Total Amount =", total)
#     print("Thank You! Visit Again")
#     print("================================")


# # Function Call
# hotel_bill()

# #2nd method : Hotel bill generator using OOPs
# class HotelBill:

#     def __init__(self):
#         self.hotel_name = "Sunshine Hotel"
#         self.total = 0
#         self.bill_items = []

#     def customer_details(self):
#         print("\n========== Sunflower HOTEL BILL ==========")
#         print("Hotel Name :", self.hotel_name)
#         self.name = input("Enter Customer Name: ")
#         self.date = input("Enter Date (dd-mm-yyyy): ")

#     def show_menu(self):
#         print("\n------ MENU ------")
#         print("1. Tea        - 10")
#         print("2. Coffee     - 40")
#         print("3. Sandwich   - 60")
#         print("4. Burger     - 80")
#         print("5. Pizza      - 120")

#     def take_order(self):
#         while True:
#             choice = int(input("\nEnter item number (0 to finish): "))

#             if choice == 0:
#                 break

#             qty = int(input("Enter quantity: "))

#             if choice == 1:
#                 item = "Tea"
#                 price = 10 * qty
#             elif choice == 2:
#                 item = "Coffee"
#                 price = 40 * qty
#             elif choice == 3:
#                 item = "Sandwich"
#                 price = 60 * qty
#             elif choice == 4:
#                 item = "Burger"
#                 price = 80 * qty
#             elif choice == 5:
#                 item = "Pizza"
#                 price = 120 * qty
#             else:
#                 print("Invalid choice")
#                 continue

#             self.bill_items.append((item, qty, price))
#             self.total += price

#     def generate_bill(self):
#         print("\n========== FINAL BILL ==========")
#         print("Customer :", self.name)
#         print("Date     :", self.date)
#         print("--------------------------------")
#         print("Item        Qty   Price")
#         print("--------------------------------")

#         for item, qty, price in self.bill_items:
#             print(f"{item:<12} {qty:<5} {price}")

#         print("--------------------------------")
#         print("Total Amount =", self.total)
#         print("Thank You! Visit Again")
#         print("================================")


# # Object creation
# obj = HotelBill()

# # Method calls
# obj.customer_details()
# obj.show_menu()
# obj.take_order()
# obj.generate_bill()


#3rd method:
#Hotel Bill Printing programme using OOPs and SQL connectivity
import pyodbc

class HotelBill:

    def __init__(self):
        self.total = 0
        self.items = []

        # Database connection
        server = r"LAPTOP-IG764KG2\SQLEXPRESS"
        database = "Hotelbill"

        connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={server};"
            f"DATABASE={database};"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )

        self.conn = pyodbc.connect(connection_string)
        self.cursor = self.conn.cursor()

    def customer_details(self):
        self.name = input("Enter customer name: ")
        self.date = input("Enter date (dd-mm-yyyy): ")

    def show_menu(self):
        print("\n------ MENU ------")
        print("1. Tea - 20")
        print("2. Coffee - 40")
        print("3. Sandwich - 70")
        print("4. Burger - 80")
        print("5. Pizza - 120")

    def take_order(self):
        while True:
            ch = int(input("\nEnter item number (0 to finish): "))
            if ch == 0:
                break

            qty = int(input("Enter quantity: "))

            if ch == 1:
                item, price = "Tea", 20 * qty
            elif ch == 2:
                item, price = "Coffee", 40 * qty
            elif ch == 3:
                item, price = "Sandwich", 70 * qty
            elif ch == 4:
                item, price = "Burger", 80 * qty
            elif ch == 5:
                item, price = "Pizza", 120 * qty
            else:
                print("Invalid choice")
                continue

            self.items.append((item, qty, price))
            self.total += price

    def save_to_db(self):
        for item, qty, price in self.items:
            query = """
            INSERT INTO Bills (item, quantity, amount)
            VALUES (?, ?, ?)
            """
            data = (item, qty, price)
            self.cursor.execute(query, data)

        self.conn.commit()

    def show_bill(self):
        print("\n------ FINAL BILL ------")
        print("Customer:", self.name)
        print("Date:", self.date)
        print("------------------------")
        print("Item      Qty     Price")

        for item, qty, price in self.items:
            print(f"{item:10} {qty:<7} {price}")

        print("------------------------")
        print("Total =", self.total)


# ---------- MAIN ----------
obj = HotelBill()
obj.customer_details()
obj.show_menu()
obj.take_order()
obj.save_to_db()
obj.show_bill()

