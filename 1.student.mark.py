print("-----Student mark management-----")
listStudents = []
listCourses = []
listMarks = []
import Labwork1 as d

def addStudent():
    print("*** Add Students ***")
    infor = {
        'id' : '',
        'name' : ''
    }
    print("Enter Student's ID:")
    id = input()
    infor['id'] = id
    print("Enter Student's Name:")
    infor['name'] = input()
    d.listStudents.append(infor)

def Mark():
    print("Enter Student's Mark:")

def addCourse():
    print("Enter Course's Name:")


