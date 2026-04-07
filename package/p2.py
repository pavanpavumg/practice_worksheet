class Employee:
    def __init__(self, name, emp_id, age, position):
        self.name, self.emp_id, self.age, self.position = name, emp_id, age, position

    def calculate_salary(self):
        pass

    def display_details(self):
        pass


class PermanentEmployee(Employee):
    def __init__(self, name, emp_id, age, position, basic_salary):
        super().__init__(name, emp_id, age, position)
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary * 1.3   # 30% extra benefits

    def display_details(self):
        print(f"\n--- Permanent Employee ---")
        print(f"Name: {self.name}, ID: {self.emp_id}, Age: {self.age}, Position: {self.position}")
        print(f"Basic Salary: {self.basic_salary}, Total Salary: {self.calculate_salary()}")


class ContractEmployee(Employee):
    def __init__(self, name, emp_id, age, position, hourly_rate, hours_worked):
        super().__init__(name, emp_id, age, position)
        self.hourly_rate, self.hours_worked = hourly_rate, hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def display_details(self):
        print(f"\n--- Contract Employee ---")
        print(f"Name: {self.name}, ID: {self.emp_id}, Age: {self.age}, Position: {self.position}")
        print(f"Hourly Rate: {self.hourly_rate}, Hours Worked: {self.hours_worked}, Total Salary: {self.calculate_salary()}")


class EmployeeDatabase:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp):
        self.employees[emp.emp_id] = emp
        print("Employee added successfully.\n")

    def view_all(self):
        if not self.employees:
            print("No employees found.\n")
            return
        for emp in self.employees.values():
            emp.display_details()

    def search(self, emp_id):
        if emp_id in self.employees:
            self.employees[emp_id].display_details()
        else:
            print("Employee not found.\n")


def main():
    db = EmployeeDatabase()
    while True:
        print("\n1. Add Permanent\n2. Add Contract\n3. View All\n4. Search by ID\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            emp = PermanentEmployee(
                input("Name: "),
                input("ID: "),
                int(input("Age: ")),
                input("Position: "),
                float(input("Basic Salary: "))
            )
            db.add_employee(emp)

        elif choice == '2':
            emp = ContractEmployee(
                input("Name: "),
                input("ID: "),
                int(input("Age: ")),
                input("Position: "),
                float(input("Hourly Rate: ")),
                float(input("Hours Worked: "))
            )
            db.add_employee(emp)

        elif choice == '3':
            db.view_all()

        elif choice == '4':
            db.search(input("Enter ID: "))

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
