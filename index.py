
class Student:
    student_Dictionary = {}
    school_name = 'XYZ'

    def __init__(self):
        self.roll_no = input("\n\tEnter the Student Roll Number: ")
        self.name = input("\t Enter the Student Name: ")
        self.phone_number = input("\t Enter the Student Phone Number: ")
        self.address = input("\t Enter the Student Address: ")
        student_class = input("\t Enter the Student class [Ex:1 2 3 4 5 6 7 8 9 10]: ")

        if student_class in StudentClass.classes:
            StudentClass.classes[student_class].studentList.append(self)
        else:
            new_class = StudentClass(student_class)
            new_class.studentList.append(self)
            StudentClass.classes[student_class] = new_class

        self.student_class = StudentClass.classes[student_class]

        print("\n Student Added Successfully")
        self.getStudent()

    def getStudent(self):
        print("\n--------Student Details-----------\n")
        print("\t Roll Number:", self.roll_no)
        print("\t Name:", self.name)
        print("\t Phone Number:", self.phone_number)
        print("\t Address:", self.address)
        print("\t Class:", self.student_class.name)
        print("\t School Name:", Student.school_name)

    def updateStudent(self):
        print("\t\tSelect an option to update student details\n")
        print("\t\t1) Change Student Name")
        print("\t\t2) Change Student Phone Number")
        print("\t\t3) Change Student Address")
        print("\t\t4) Change Student Class")
        option = input("\t\t Enter one of the above options: ")

        if option in ['1', '2', '3', '4']:
            if option == '1':
                self.name = input("\t\t Enter the Student New Name: ")
                print("\n\t\t Student Name Changed Successfully\n")
            elif option == '2':
                self.phone_number = input("\t\t Enter the Student New Phone Number: ")
                print("\n\t\t Student Phone Number Changed Successfully\n")
            elif option == '3':
                self.address = input("\t\t Enter the Student New Address: ")
                print("\n\t\t Student Address Changed Successfully\n")
            elif option == '4':
                new_class = input("\t\t Enter the New Class Name: ")
                self.student_class.studentList.remove(self)
                if new_class in StudentClass.classes:
                    self.student_class = StudentClass.classes[new_class]
                    self.student_class.studentList.append(self)
                else:
                    add_class = StudentClass(new_class)
                    add_class.studentList.append(self)
                    self.student_class = add_class
                print("\n\t\t Student Class Changed Successfully\n")

            self.getStudent()
        else:
            print("\n\t You have chosen a wrong option")

    @classmethod
    def updateSchoolName(cls, new_school_name):
        cls.school_name = new_school_name

    @classmethod
    def getTotalStudentCount(cls):
        return len(cls.student_Dictionary)


class StudentClass:
    classes = {}

    def __init__(self, name):
        self.name = name
        self.studentList = []
        StudentClass.classes[name] = self


def main():
    print(f"----------- Welcome to {Student.school_name} School ----------\n")
    print("\t1) Get Student Details")
    print("\t2) Add Student")
    print("\t3) Remove Student")
    print("\t4) Update Student Details")
    print("\t5) Update School Name")
    print("\t6) Get Number of Students in School")
    print("\t7) Get All Student Details")
    print("\t8) Get Class Student Details")

    option = input("Enter one of the above options: ")

    if option == '1':
        roll_no = input("\tEnter the Roll Number of a Student: ")
        try:
            Student.student_Dictionary[roll_no].getStudent()
        except KeyError:
            print("\t You have entered the wrong roll number")
    elif option == '2':
        new_student = Student()
        Student.student_Dictionary[new_student.roll_no] = new_student
    elif option == '3':
        roll_no = input("\tEnter the Roll Number of a Student to remove: ")
        try:
            student = Student.student_Dictionary.pop(roll_no)
            student.student_class.studentList.remove(student)
            print(f"\t\t Student with Roll Number {roll_no} Deleted Successfully")
        except KeyError:
            print("\t\t No Student found with that roll number")
    elif option == '4':
        roll_no = input("\t Enter the Roll Number of the Student: ")
        try:
            Student.student_Dictionary[roll_no].updateStudent()
        except KeyError:
            print("\t\t You have entered the wrong roll number")
    elif option == '5':
        new_school_name = input("\tEnter the New School Name: ")
        Student.updateSchoolName(new_school_name)
        print("\t\t School Name Changed Successfully")
    elif option == '6':
        print(f"\t\t Total Number of Students: {Student.getTotalStudentCount()}")
    elif option == '7':
        if Student.student_Dictionary:
            print(f"\t\t Total Number of Students: {Student.getTotalStudentCount()}")
            print("\n Total Student List with Details\n")
            for s_no, student in enumerate(Student.student_Dictionary.values(), start=1):
                print(f"Student-{s_no}")
                student.getStudent()
                print()
        else:
            print("\t\t No Students available")
    elif option == '8':
        class_name = input("\t Enter the Class Name: ")
        try:
            students = StudentClass.classes[class_name]
            print(f"\n Total Number of Students in Class {class_name}: {len(students.studentList)}\n")
            for s_no, student in enumerate(students.studentList, start=1):
                print(f"\t Student {s_no}")
                student.getStudent()
                print()
        except KeyError:
            print("\nYou entered the wrong class or no students are in that class")


if __name__ == '__main__':
    option = 'y'
    while option.lower() == 'y':
        main()
        option = input("\n Do You Want to Continue? [y/n]: ")
        print()
