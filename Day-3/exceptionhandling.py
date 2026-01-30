class StudentInfo:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

class Marks:
    def __init__(self):
        self.marks = None

    def input_marks(self):
        try:
            self.marks = float(input("Enter marks: "))
            if self.marks < 0 or self.marks > 100:
                raise ValueError("Marks must be between 0 and 100")
        except ValueError as e:
            print(f"Invalid input: {e}")
            self.marks = None

    def get_status(self):
        if self.marks is None:
            return "No valid marks entered"
        if self.marks == 0:
            return "Absent"
        elif self.marks >= 70:
            return "Pass"
        else:
            return "Fail"

class InterviewMarks(Marks):
    def __init__(self):
        super().__init__()

def main():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    student = StudentInfo(name, roll_no)

    print("\nEnter regular marks:")
    regular_marks = Marks()
    regular_marks.input_marks()

    print("\nEnter interview marks:")
    interview_marks = InterviewMarks()
    interview_marks.input_marks()
    student.display()
    print(f"Regular Exam Status: {regular_marks.get_status()}")
    print(f"Interview Status: {interview_marks.get_status()}")

if __name__ == "__main__":
    main()