class Student:
    def __init__(self):
        self._usn = None
        self._name = None
        self._branch = None
        self._phone = None
    def accept(self):
        self._usn = input("Enter usn: ")
        self._name = input("Enter name: ")
        self._branch = input("Enter branch: ")
        self._phone = input("Enter phone: ")
    def display(self):
        print("USN:", self._usn)
        print("Name:", self._name)
        print("Branch:", self._branch)
        print("Phone:", self._phone)

if __name__ == '__main__':
    n = int(input("Enter number of students: "))
    students = []
    for i in range(n):
        x = Student()
        x.accept()
        students.append(x)
    print("\nDisplaying data:")
    for emt in students:
        emt.display()
