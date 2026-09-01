import csv
import json
from student import Student


def read_txt(file):
    students = []

    with open(file, "r") as f:
        lines = f.readlines()

    for line in lines:
        data = line.strip().split(",")

        if len(data) == 7:
            s = Student(
                int(data[0].strip()),
                data[1].strip(),
                data[2].strip(),
                int(data[3].strip()),
                int(data[4].strip()),
                int(data[5].strip()),
                int(data[6].strip())
            )
            students.append(s)

    return students


def write_txt(file, students):
    with open(file, "w") as f:
        for s in students:
            f.write(
                f"{s.student_id}, {s.name}, {s.department}, "
                f"{s.semester}, {s.mark1}, {s.mark2}, {s.mark3}\n"
            )


def read_csv(file):
    students = []

    with open(file, "r", newline="") as f:
        reader = csv.reader(f)

        next(reader, None)

        for data in reader:
            if len(data) == 7:
                s = Student(
                    int(data[0]),
                    data[1],
                    data[2],
                    int(data[3]),
                    int(data[4]),
                    int(data[5]),
                    int(data[6])
                )
                students.append(s)

    return students


def write_csv(file, students):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "Student_ID",
            "Name",
            "Department",
            "Semester",
            "Subject1",
            "Subject2",
            "Subject3"
        ])

        for s in students:
            writer.writerow([
                s.student_id,
                s.name,
                s.department,
                s.semester,
                s.mark1,
                s.mark2,
                s.mark3
            ])


def read_json(file):
    students = []

    with open(file, "r") as f:
        data = json.load(f)

    for item in data:
        s = Student(
            item["student_id"],
            item["name"],
            item["department"],
            item["semester"],
            item["marks"]["subject1"],
            item["marks"]["subject2"],
            item["marks"]["subject3"]
        )
        students.append(s)

    return students


def write_json(file, students):
    data = []

    for s in students:
        item = {
            "student_id": s.student_id,
            "name": s.name,
            "department": s.department,
            "semester": s.semester,
            "marks": {
                "subject1": s.mark1,
                "subject2": s.mark2,
                "subject3": s.mark3
            }
        }

        data.append(item)

    with open(file, "w") as f:
        json.dump(data, f, indent=4)

