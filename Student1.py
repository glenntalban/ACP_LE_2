# Student class
class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        # Tuple (id, name) for student basic info (immutable)
        self.id_name = (student_id, student_name)
        # String email of student
        self.email = email
        # Dictionary grades, default empty if not given
        self.grades = grades if grades is not None else {}
        # Set courses enrolled, default empty if not given
        self.courses = courses if courses is not None else set()

    # Return format string when containing the student info
    def __str__(self):
        return (f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, "
                f"Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}, GPA: {self.calculate_gpa():.2f}")
    
     # Calculate the GPA from grades
    def calculate_gpa(self):
        gpa_scale = {
            (90, 100): 1.0,
            (80, 89): 2.0,
            (70, 79): 3.0,  # Convert their grades into GPA scale
            (60, 69): 4.0,
            (0, 59): 0.0
        }

        total_points = 0
        total_courses = len(self.grades)

        # No grades yet
        if not self.grades:
            return 0.0  

        for subject, grade in self.grades.items():
            for score_range, gpa in gpa_scale.items():
                if score_range[0] <= grade <= score_range[1]:
                    total_points += gpa
                    break
        if total_courses > 0:
            # Average GPA = total points / number of courses
            return total_points / total_courses
        else:
            return 0.0
        
# Studentrecord class
class StudentRecords:
    def __init__(self):
        # list hold multiple student objects
        self.students = []

    # Add student
    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        student = Student(student_id, student_name, email, grades, courses)
        self.students.append(student)
        return "Student added successfully" # Str message indicating that the student was added successfully
    
    # Update a existing student info
    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.id_name[0] == student_id:
                if email:
                    student.email = email
                if grades:
                    student.grades = grades  # dictionary
                if courses:
                    student.courses = courses
                return "Student updated successfully"
        return "Student not found"
    
    # Delete student
    def delete_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                self.students.remove(student)
                return "Student deleted successfully"
        return "Student not found"
    
    # Enroll Course for Student
    def enroll_course(self, student_id, course):
        for student in self.students:
            if student.id_name[0] == student_id:
                student.courses.add(course)
                return "Course enrolled successfully"
        return "Student not found"
    
    # Search Student by their ID
    def search_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                return str(student)
        return "Student not found"
    
    # Search for student by a partial match of their name
    def search_by_name(self, name):
        matches = []
        for student in self.students:
            if name.lower() in student.id_name[1].lower():
                matches.append(str(student))
        return matches if matches else "Student not found"

# Program
records = StudentRecords()
print(records.add_student(24, "glenn", "glenn@mail.com", {"DBMS": 92,}, {"IT211"}))
print(records.add_student(25, "ford", "ford@mail.com", {"DISCRETE MATH": 84}, {"CPE405"}))
print(records.add_student(26, "bughaw", "bughaw@gmail.com", {"OOP": 80}, {"CS211"}))
print(records.add_student(27, "talban", "talban@gmail.com", {"ACP": 85}, {"CS121"}))

# Search by the ID
print(f"Student with {records.search_student(24)}") # glenn GPA
print(f"Student with {records.search_student(25)}") # ford GPA

# Update Ford's info
print(records.update_student(25, grades={"DISCRETE MATH": 90}, courses={"CPE405"})) # Updated GPA
print(f"Updated student with {records.search_student(25)}")  

# Enroll glenn in IT211
print(records.enroll_course(24, "IT211"))
print(f"Student with {records.search_student(24)}")

# Delete talban info
print(records.delete_student(27))
print(records.search_student(27))

# Partial name search
print("Search results of student for 'glenn':")
for s in records.search_by_name("glenn"):
    print(s) 
        
        
