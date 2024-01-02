class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}

# оценка лектора:
  def rate_lc(self, lecturer, course, grade):
      if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
          if course in lecturer.grades:
              lecturer.grades[course] += [grade]
          else:
              lecturer.grades[course] = [grade]
      else:
          return 'Not found'

    
   # переопределяем __str__
  def __str__(self):
     return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"

# def add_courses(self, course_name):
  #     self.finished_courses.append(course_name)   

class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []

  
class Lecturer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)
      self.grades = {}

   # переопределяем __str__
  
  def __str__(self):
     return f"Имя: {self.name}\nФамилия: {self.surname}" 

# средняя оценка за лекции
  
  # def middle_rate():

class Reviewer(Mentor):    
  def __init__(self, name, surname):
    super().__init__(name, surname)
   
  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in Mentor.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'

  # переопределяем __str__

  def __str__(self):
     return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: " 
    
 # Students

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']

best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

best_student.grades['Git'] = [10, 10, 10, 9, 10]
best_student.grades['Python'] = [8, 10]

one_student = Student('Stew', 'Dent', 'some gender')
one_student.finished_courses += ['Java']
one_student.finished_courses += ['Git']

one_student.courses_in_progress += ['Python']

one_student.grades['Git'] = [10, 10, 7, 9, 10]
one_student.grades['Python'] = [8, 7, 10]

print(one_student)

#  Lecturers

cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

# some_reviewer = Reviewer ('Revi', 'Ewer')
# print(some_reviewer)

some_lecturer = Lecturer ('Lec', 'Tor')
some_lecturer.courses_attached += ['Java', 'C++']