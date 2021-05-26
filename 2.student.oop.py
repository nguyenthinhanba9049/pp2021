def option():
    print("1. Set infor for student: ")
    print("2. Set infor for course: ")
    print("3. Set mark  student by course: ")
    print("4. Get infor for student: ")
    print("5. Get infor for course: ")
    print("6. Get infor for student course management: ")
    print("0. Exit.")


print("Program started !!!")
option()
choice = int(input("Enter number(0-6) choice: "))

while choice != 0:
    if choice == 1:
        choice1()
        quit_menu()

    elif choice == 2:
        choice2()
        quit_menu()

    elif choice == 3:
        choice3()
        quit_menu()

    elif choice == 4:
        print("information of student in class: ")
        for i in st_list:
            print("Student's name = " + i.get_st_name(), end=". ID = ")
            print(i.get_st_id(), end=". DoB = " + i.get_st_dob())
            print()
        quit_menu()

    elif choice == 5:
        print("information of course: ")
        for i in course_list:
            print("Course's name = " + i.get_name(), end=". ID = ")
            print(i.get_id())
        quit_menu()

    elif choice == 6:
        for i in mark_list:
            print("This is mark of " + i.get_st_name() + ": ", end="")
            print(i.get_crs_inf())
        quit_menu()

    else:
        print("You are exit.")
        break
class Student:
    def __init__(self, name, s_id, dob):
        self._stdName = name
        self._stdID = s_id
        self._stdDoB = dob

    def set_st_name(self, name):
        self._stdName = name

    def set_st_id(self, std_id):
        self._stdID = std_id

    def set_st_dob(self, dob):
        self._stdDoB = dob

    def get_st_name(self):
        return self._stdName

    def get_st_id(self):
        return self._stdID

    def get_st_dob(self):
        return self._stdDoB


class Course:
    def __init__(self, name, C_ID):
        self._name = name
        self._id = C_ID

    def set_c_name(self, name):
        self._name = name

    def set_c_id(self, C_ID):
        self._id = C_ID

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id


class Mark:
    _Student_name = ""
    _Course_inf = {}

    def __init__(self):
        pass

    def set_inf(self, name, course_inf):
        self._Student_name = name
        self._Course_inf = course_inf

    def set_st_name(self, student_name):
        self._Student_name = student_name

    def get_st_name(self):
        return self._Student_name

    def set_crs_inf(self, dic_inf):
        self._Course_inf = dic_inf

    def get_crs_inf(self):
        return self._Course_inf


# ------------------------------ database -------------------------------------
st_list = [Student("#", "#", "#")]
course_list = [Course("#", "#")]
mark_list = [Mark()]

st_list.clear()
course_list.clear()
mark_list.clear()

count_mark = 0


# ------------------------------ method -------------------------------------


def input_domain(value, min_value, max_value):
    while value < min_value or value > max_value:
        value = int(input("Your input is invalid! Enter again: "))
    return value


def quit_menu():
    global choice
    print("---------------------End of this choice---------------------")
    choice = int(input("Make other choice, 0 to quit: "))
    choice = input_domain(choice, 0, 6)
    if choice == 0:
        print("You choose quit! Thank for using my program.")


def choice1():
    global i
    num_of_st = int(input("Enter number of student in the class: "))
    for i in range(0, num_of_st):
        name = str(input("Enter student name: "))
        s_id = str(input("Enter student id: "))
        dob = str(input("Enter student dob: "))
        st_list.append(Student(name, s_id, dob))


def choice2():
    global i
    num_of_cour = int(input("Enter number of course: "))
    for i in range(0, num_of_cour):
        c_name = str(input("Enter course name: "))
        C_ID = str(input("Enter course id: "))
        course_list.append(Course(c_name, C_ID))


def choice3():
    global choice, i, count_mark
    name = str(input("Enter name of student want to manage: "))
    cour_inf_lit = {}
    if checkStList(name):
        mark_list.append(Mark())
        mark_list[count_mark].set_st_name(name)
        num_of_cour = int(input("Enter number of courses this student studied: "))
        for i in range(0, num_of_cour):
            c_name = input("Enter name of course: ")
            if checkCourList(c_name):
                mark = int(input("Enter mark of this course: "))
                cour_inf_lit[c_name] = mark
                mark_list[count_mark].set_crs_inf(cour_inf_lit)
            else:
                print("Input course did not import.")
        count_mark = count_mark + 1
    else:
        choice = int(input("Input wrong ! Press 3 to do again, 0 to quit: !"))


def checkStList(name):
    global i

    check = False
    for i in st_list:
        if name == i.get_st_name():
            check = True
    return check


def checkCourList(c_name):
    global i
    for i in course_list:
        if i.get_name() == c_name:
            return True
