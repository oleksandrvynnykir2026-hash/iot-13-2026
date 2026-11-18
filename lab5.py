class Student:
    
    def __init__(self, first_name: str, last_name: str, student_id: str, grades: list = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.grades = grades if grades is not None else []

    def __del__(self) -> None:
        pass

    def get_average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def display_info(self) -> None:
        avg = self.get_average_grade()
        print(f"Студент: {self.last_name} {self.first_name} | ID: {self.student_id} | Середній бал: {avg:.2f}")


class Group:
    
    def __init__(self, group_name: str, students: list = None) -> None:
        self.group_name = group_name
        self.students = students if students is not None else []

    def __del__(self) -> None:
        pass

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def display_group(self) -> None:
        print(f"--- Група: {self.group_name} ---")
        for student in self.students:
            student.display_info()


if __name__ == "__main__":
    student1 = Student("Олександр", "Винник", "IP-1301", [90, 85, 95, 88])
    student2 = Student("Іван", "Петренко", "IP-1302", [75, 80, 82, 78])

    group = Group("ІР-13")
    group.add_student(student1)
    group.add_student(student2)

    group.display_group()