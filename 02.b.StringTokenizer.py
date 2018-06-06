class Customer:
    def __init__(self):
        self.name = None
        self.dob = None

    def accept(self):
        self.name, self.dob = input("Enter name and dob:\n").split(", ")
    def display(self):
        date, month, year = self.dob.split("/")
        print(self.name, date, month, year)

if __name__ == "__main__":
    C = Customer()
    C.accept()
    C.display()
