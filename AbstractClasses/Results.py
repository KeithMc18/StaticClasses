
class Results:

    def __init__(self, module_name_in, grade_in):
        self.module_name = module_name_in
        self.grade = grade_in


class Student:

    def __init__(self, name_in, x_number_in):
        self.name = name_in
        self.x_number = x_number_in
        self.results = []

    def add_results(self, results_in):
        self.results.append(results_in)

    def print(self):


results1 = Results('python', 100)

student1 = Student('keith', 'x00158262')

student1.add_results(results1)

