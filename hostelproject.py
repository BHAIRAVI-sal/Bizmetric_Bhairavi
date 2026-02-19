class MasterDegreeFees:

    def __init__(self, subject, analytics, hostel, food_months, transport_type):
        self.subject = subject.upper()
        self.analytics = analytics.upper()
        self.hostel = hostel.upper()
        self.food_months = food_months
        self.transport_type = transport_type.lower()

        self.total_fee = 0

    def calculate_fee(self):

        try:
           
            base_fee = 200000
            self.total_fee += base_fee

           
            if self.subject in ["HR", "MARKETING"]:
                if self.analytics == "Y":
                    self.total_fee += base_fee * 0.10

            elif self.subject == "DS":
                if self.analytics == "Y":
                    raise ValueError("DS does not have analytics option")

            
            if self.hostel == "Y":
                self.total_fee += 200000

            
            self.total_fee += self.food_months * 2000

           
            if self.transport_type == "semester":
                self.total_fee += 13000 * 2
            elif self.transport_type == "annual":
                self.total_fee += 26000
            else:
                raise ValueError("Invalid transport type")

            return self.total_fee

        except Exception as e:
            return f"Error : {e}"


while True:
    try:
        subject = input("Enter Subject (HR / Finance / Marketing / DS): ").upper()
        if subject not in ["HR", "FINANCE", "MARKETING", "DS"]:
            raise ValueError
        break
    except:
        print("Invalid Subject! Try again.")

while True:
    try:
        analytics = input("Do you want Analytics? (Y/N): ").upper()
        if analytics not in ["Y", "N"]:
            raise ValueError
        break
    except:
        print("Invalid input! Enter Y or N.")

while True:
    try:
        hostel = input("Do you want Hostel? (Y/N): ").upper()
        if hostel not in ["Y", "N"]:
            raise ValueError
        break
    except:
        print("Invalid input! Enter Y or N.")
while True:
    try:
        food_months = int(input("Enter food months (0-12): "))
        if food_months < 0 or food_months > 12:
            raise ValueError
        break
    except:
        print("Invalid input! Enter value between 0 to 12.")

while True:
    try:
        transport_type = input("Transportation type (semester/annual): ").lower()
        if transport_type not in ["semester", "annual"]:
            raise ValueError
        break
    except:
        print("Invalid input! Enter semester or annual.")

student = MasterDegreeFees(subject, analytics, hostel, food_months, transport_type)

total = student.calculate_fee()

print("\n Total Annual Fees =", total)
