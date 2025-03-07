class Course():
    def __init__(self, name:str, grade:int, credits:int):
        self.name = name
        self.grade = grade
        self.credits = credits

class CourseTracker():
    def __init__(self):
        self.course_list = []

    def add_course(self):
        name = input("course name: ")
        grade = input("course grade: ")
        credits = input("course credits: ")
        course = Course(name, grade, credits)
        self.course_list.append(course)

    def get_data(self):
        name = input("course name: ")
        flag = False
        for course in self.course_list:
            if course.name == name:
                flag = True
                print(course.name, course.grade, course.credits)
            if flag == False:
                print("no course name in database")
    def stats(self):
        credit_sum = 0
        grade_dict = {}
        for course in self.course_list:
            credit_sum += int(course.credits)
            if course.grade not in grade_dict.keys():
                grade_dict[course.grade] = 0
            else:
                grade_dict[course.grade] += 1
    
        print(f"{len(self.course_list)} completed courses for a total credits of {credit_sum}")
        print(f"mean {credit_sum / len(self.course_list)}")
        print("grade distribution: ")
        for grade, count in grade_dict.items():
            print(f"{grade}: {''.join(['x' for i in (range(count+1))])}")
        


class CourseTrackerApplication():
    def __init__(self):
        self.__coursetracker = CourseTracker()

    def help(self):
        print("commands: ")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command =="1":
                self.__coursetracker.add_course()
            elif command == "2":
                self.__coursetracker.get_data()
            elif command == "3":
                self.__coursetracker.stats()


cta = CourseTrackerApplication()
cta.execute()