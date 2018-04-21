class Staff:
    def __init__(self):
        self.staffid = None
        self.name = None
        self.phone = None
        self.salary = None

    def accept(self):
        self.staffid = input("Enter StaffID: ")
        self.name = input("Enter name: ")
        self.phone = input("Enter phone: ")
        self.salary = input("Enter salary: ")

    def display(self):
        print("StaffID:", self.staffid)
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Salary:", self.salary)

class Teaching(Staff):
    def __init__(self):
        self.domain = None
        self.publications = []

    def accept(self):
        super().accept()
        self.domain = input("Enter domain: ")
        n = int(input("Enter number of publications: "))
        print("Enter publications: ")
        for _ in range(n):
            self.publications.append(input())

    def display(self):
        super().display()
        print("Domain:", self.domain)
        print("Publications:", )
        for publication in self.publications:
            print(publication, end = " ")

class Technical(Staff):
    def __init__(self):
        self.skills = []

    def accept(self):
        super().accept()
        n = int(input("Enter number of skills: "))
        print("Input skills: ")
        for _ in range(n):
            self.skills.append(input())

    def display(self):
        super().display
        for skill in self.skills:
            print(skill, end = " ")

class Contract(Staff):
    def __init__(self):
        self.period = 0

    def accept(self):
        super().accept()
        self.period = input("Enter contract period: ")

    def display(self):
        super().display()
        print("Contract period:", self.period)

if __name__ == '__main__':
    teaching = Teaching()
    technical = Technical()
    contract = Contract()

    print("Enter details for teaching staff: ")
    teaching.accept()
    print("Enter details for technical staff: ")
    technical.accept()
    print("Enter details for staff on contract: ")
    contract.accept()

    print(end = "\n")

    print("Details for teaching staff: ")
    teaching.display()
    print("\nDetails for technical staff: ")
    technical.display()
    print("\nDetails for staff on contract: ")
    contract.display()
