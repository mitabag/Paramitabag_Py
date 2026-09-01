import argparse
from manager import StudentManager
def main():
    parser = argparse.ArgumentParser(
        description="Student Record Management System"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Name of the student data file"
    )

    parser.add_argument(
        "--format",
        required=True,
        choices=["txt", "csv", "json"],
        help="File format"
    )

    args = parser.parse_args()

    manager = StudentManager()

    print("Student Record Management System")
    print("File:", args.file)
    print("Format:", args.format)
    manager.load_from_file(args.file, args.format)
    manager.display_all_students()


if __name__ == "__main__":
    main()