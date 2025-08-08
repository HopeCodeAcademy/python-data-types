class Employer:
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry

    def display_info(self):
        print(f"Employer: {self.name}-{self.industry}")


employer_one = Employer("HopeCode", "Technology")
employer_one.display_info()
