class Employer:
    def __init__(self, employee_count):
        self.__employee_count = employee_count
    
    def get_employee_count(self):
        return self.__employee_count

    
employer_one = Employer(1500)

print("No. of Employees:", employer_one.get_employee_count())

print("No. of Employees (Accessing via Name Mangling):", employer_one._Employer__employee_count )

