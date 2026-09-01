class Student:
    def __init__(self, student_id: int, name: str, department: str,
                 semester: str, mark1: int, mark2: int, mark3: int):

        self.student_id = student_id
        self.name = name
        self.department = department
        self.semester = semester
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calculate_total(self):
        return self.mark1 + self.mark2 + self.mark3

    def calculate_average(self):
        return self.calculate_total() / 3

    def get_result(self):
        if self.mark1 < 33 or self.mark2 < 33 or self.mark3 < 33:
            return "Fail"
        return "Pass"

    def update_marks(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def update_name(self, name):
        self.name = name

    def update_semester(self, semester):
        self.semester = semester

    def display_student(self):
        print("Student Record")
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Semester: {self.semester}")
        print(f"Marks: {self.mark1}, {self.mark2}, {self.mark3}")
        print(f"Total: {self.calculate_total()}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Result: {self.get_result()}")


if __name__ == "__main__":

    student1 = Student(
        101,
        "Rahul",
        "Computer Science",
        "1",
        78,
        82,
        69
    )

    student2 = Student(
        102,
        "Priya",
        "Computer Science",
        "1",
        91,
        87,
        94
    )

    student3 = Student(
        103,
        "Amit",
        "Mathematics",
        "1",
        65,
        71,
        68
    )

    student1.display_student()
    student2.display_student()
    student3.display_student()