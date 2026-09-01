from student import Student
import file_handler

class StudentManager:

    def __init__(self):
        self.st = []

    def add(self, s):
        self.st.append(s)

    def search(self, sid):
        for s in self.st:
            if s.student_id == sid:
                return s
        return None

    def remove(self, sid):
        s = self.search(sid)

        if s:
            self.st.remove(s)
            print("Student removed.")
        else:
            print("Student not found.")

    def display(self):
        for s in self.st:
            s.display_student()

    def display_all_students(self):
        self.display()

    def update(self, sid, m1, m2, m3):
        s = self.search(sid)

        if s:
            s.update_marks(m1, m2, m3)
            print("Marks updated.")
        else:
            print("Student not found.")

    def load_from_file(self, file, fmt):
        if fmt == "txt":
            self.st = file_handler.read_txt(file)

        elif fmt == "csv":
            self.st = file_handler.read_csv(file)

        elif fmt == "json":
            self.st = file_handler.read_json(file)

    def save_to_file(self, file, fmt):
        if fmt == "txt":
            file_handler.write_txt(file, self.st)

        elif fmt == "csv":
            file_handler.write_csv(file, self.st)

        elif fmt == "json":
            file_handler.write_json(file, self.st)

