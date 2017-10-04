def main():
  students = [
    Student("Larsson", "Jerome", "37"),
    Student("BonJovi", "Billy", "55"),
    Student("David", "Larry", "97"),
  ]

  printHeader()
  selection = getUserSelection()
  if selection == 0:
    printStudentsByAge(students)
  elif selection == 1:
    printStudentsByLName(students)
  elif selection == 2:
    printStudentsByFName(students)
  elif selection == 3:
    printSumAge(students)
  else:
    print ("SELECTION NOT RECOGNIZED")


class Student:
  def __init__(self, lastName, firstName, age):
    self.lastName = lastName
    self.age = age
    self.firstName = firstName

  def assignRandomName(self):
    
    pass

  def assignRandomAge(self):
    self.age = random.randint(0,100)

  def assignRandomWeight(self, isMetric):
    pass

  def assignRandomHeight(self, isMetric):
    pass

inputQuestions = [ 
  "For STUDENTS BY AGE, type 0",
  "For STUDENTS BY LAST NAME, type 1",
  "For STUDENTS BY FIRST NAME, type 2",
  "For SUM of STUDENT AGES type 3",
  "For AVERAGE of STUDENT AGES type 4",
]

def getUserSelection():
  print (inputQuestions[0])
  print (inputQuestions[1])
  print (inputQuestions[2])
  print (inputQuestions[3])
  return int(input("Type selection and press enter:"))

def printHeader():
    print("Student Analyzer")

def printStudentsByAge(students):
  print ("----Students By Age-----")
  sortStudents = sorted(students, key=lambda student: student.age)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age))

def printStudentsByLName(students):
  print ("----Students By Last Name-----")
  sortStudents = sorted(students, key=lambda student: student.lastName)
  for student in sortStudents:
    print (student.firstName + ", " + student.age + ", " + str(student.lastName))

def printStudentsByFName(students):
  print ("----Students By First Name-----")
  sortStudents = sorted(students, key=lambda student: student.firstName)
  for student in sortStudents:
    print (student.lastName + ", " + student.age + ", " + str(student.firstName))

def printSumAge(students):
  print ("Answer:")

def printAvgAge(students):
  print ("Answer:")

def ageRange(studentA, studentB):
  return math.abs(studentA.age - studentB.age)


main()