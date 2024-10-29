# შექმენით კლასი სახელწოდებით Student ატრიბუტებით, როგორიცაა name, student_id და courses
# (კურსების სია, რომელშიც სტუდენტი არის ჩარიცხული).
# აღწერეთ სტუდენტის ინფორმაციის და კურსების ჩვენების მეთოდები.
# შექმენით რამდენიმე ობიექტი და დაარეგისტრირეთ სხვადასხვა კურსებზე.


class Student:

    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id
        self.courses = courses

    def get_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")

    def get_course_list(self):
        print(f"{self.name}'s Courses: {', '.join(self.courses)}")

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in {course}")

    def leave_course(self, course):
        self.courses.remove(course)
        print(f"{self.name} has left the {course} course")

student1 = Student("Nika", 1, ["History", "Geography", "Science"])

student1.get_info()
student1.get_course_list()
student1.enroll("Economics")
student1.leave_course("History")
student1.get_course_list()


student2 = Student("Giorgi", 2, ["German", "Programming", "Chemistry", "English"])
student2.get_info()
student2.get_course_list()
student2.enroll("Spanish")
student2.enroll("Biology")
student2.get_course_list()
student2.leave_course("English")
student2.get_course_list()