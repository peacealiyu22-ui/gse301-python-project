"""
GSE301 Data Science: Python Fundamentals
Student Academic Performance Analysis System
Author: Aliyu Peace
Matric: 22/40IA017
"""

#PART 1: DATA COLLECTION AND STORAGE

# Task 1.1:
student_name = "Aliyu Peace"
matric_number = "22/40IA017"
age = 19
cgpa = 4.98
is_active = True
courses_registered = ["GSE301", "PUL301", "BUL301", "PUL303", "PPL301", "GNS311", "ISL309"]  # list of strings
grades = {"GSE301": "A", "PUL301": "A", "BUL301": "A", "PUL303": "A", "PPL301": "A", "GNS311": "A", "ISL309": "B"}

# Task 1.2:
# List of student names
student_names = ["Okpala Isaac", "Adeoye Kehinde", "Oyedele Yusuf", "Ekieye Bibian", "Jagaba Shamu"]

# Each student's full profile
students = {
    "Aliyu Peace": {
        "matric": "22/40IA017",
        "age": 19,
        "cgpa": 4.98,
        "is_active": True,
        "courses": ["GSE301", "PUL301", "BUL301", "PUL303", "PPL301"],
        "grades": {"GSE301": "A", "PUL301": "A", "BUL301": "A", "PUL303": "A", "PPL301": "A"}
    },
    "Okpala Isaac": {"matric": "21/55DZ059",
    "age": 20,
    "cgpa": 5.0,
    "is_active": True,
    "courses": ["GSE301", "STA301", "CSC321", "GNS311"],
    "grades":{"GSE301": "A", "STA301": "A", "CSC321": "A", "GNS311": "A"}
    },
    "Adeoye Kehinde": {
        "matric": "22/70DZ093",
        "age": 20,
        "cgpa": 3.45,
        "is_active": True,
        "courses": ["CSC321", "STA124", "STA302", "GSE301"],
        "grades": {"CSC321": "B", "STA124": "B", "STA301": "A", "GSE301": "C"}
    },
    "Oyedele Yusuf": {
        "matric": "21/55DZ032",
        "age": 19,
        "cgpa": 2.4,
        "is_active": True,
        "courses": ["STA211", "MAT213", "GNS311"],
        "grades": {"STA211": "C", "MAT213": "D", "GNS311": "C"}
    },
    "Ekieye Bibian": {
        "matric": "22/70XY066",
        "age": 18,
        "cgpa": 3.8,
        "is_active": False,
        "courses": ["CSC145", "STA301", "GSE301", "CSC101"],
        "grades": {"CSC145": "A", "STA301": "B", "GSE301": "B", "CSC101": "B"}
    },
    "Jagaba Shamu": {
        "matric": "24/90FD089",
        "age": 19,
        "cgpa": 4.2,
        "is_active": True,
        "courses": ["CSC112", "MAT101", "STA115", "GNS311"],
        "grades": {"CSC112": "A", "MAT101": "B", "STA115": "A", "GNS311": "B"}
    }
}

# Unique courses offered in the department
unique_courses = set()
for student in students.values():
    for course in student["courses"]:
        unique_courses.add(course)

# Fixed department information
department_info = ("Department of Computer Science", "Faculty of Technology", 2025)

# PART 2: DATA PROCESSING AND LOGIC

# Task 2.1:
def get_grade(score):
    """
    Convert score (0-100) to letter grade
    """
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

def get_feedback(grade):
    """
    Provide feedback based on grade using MATCH CASE
    """
    match grade:
        case "A":
            return "Excellent! Keep up the good work!"
        case "B":
            return "Very good! You're doing well!"
        case "C":
            return "Good, but there's room for improvement."
        case "D":
            return "Passing grade, but you need to work harder."
        case "E":
            return "Barely passing. Consider seeking help."
        case "F":
            return "Failed. Please retake the course."
        case _:
            return "Invalid grade"

# Task 2.2:
def get_valid_input():
    """
    Get age and CGPA from user with validation
    """
    try:
        # Get input as strings
        age_str = input("Enter student's age: ")
        cgpa_str = input("Enter student's CGPA (0.0-5.0): ")
        
        # Type conversion
        age = int(age_str)
        cgpa = float(cgpa_str)
        
        # Validation
        if not (16 <= age <= 40):
            print("Error: Age must be between 16 and 40")
            return None, None
        
        if not (0.0 <= cgpa <= 5.0):
            print("Error: CGPA must be between 0.0 and 5.0")
            return None, None
        
        return age, cgpa
        
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return None, None

# PART 3: ANALYSIS AND REPORTING

# Task 3.1:
def demonstrate_slicing():
    """
    Demonstrate list slicing operations
    """
    assignment_scores = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]
    
    print("\n=== List Slicing Operations ===")
    print(f"Original scores: {assignment_scores}")
    print(f"Top 3 scores: {assignment_scores[:3]}")  # First 3
    print(f"Last 5 scores: {assignment_scores[-5:]}")  # Last 5
    print(f"Every other score: {assignment_scores[::2]}")  # Step by 2
    
    return assignment_scores

# Task 3.2: Set Operations
def demonstrate_set_operations():
    """
    Demonstrate set operations
    """
    # Students who passed GSE301 (grade A, B, C, D, or E)
    set_pass = set()
    # Students with CGPA above 4.0
    set_merit = set()
    
    for student_name, student_data in students.items():
        # Check for merit (CGPA > 4.0)
        if student_data["cgpa"] > 4.0:
            set_merit.add(student_name)
        
        # Check if student passed GSE301 (if they took it)
        if "GSE301" in student_data["grades"]:
            grade = student_data["grades"]["GSE301"]
            if grade in ["A", "B", "C", "D", "E"]:
                set_pass.add(student_name)
    
    print("\n" + "="*50)
    print("Set Operations")
    print("="*50)
    print(f"Students who passed GSE301: {set_pass}")
    print(f"Students with CGPA > 4.0: {set_merit}")
    print(f"Passed AND have merit (intersection): {set_pass.intersection(set_merit)}")
    print(f"All students in both sets (union): {set_pass.union(set_merit)}")
    print(f"Passed but NO merit (difference): {set_pass.difference(set_merit)}")
    
    return set_pass, set_merit

# PART 4: INTERACTIVE MENU SYSTEM

# Task 4.1: Build a Console Menu
def display_menu():
    """
    Display the main menu
    """
    print("\n" + "="*50)
    print("Student Academic Performance System")
    print("="*50)
    print(f"{len(students)} student profiles loaded.")
    print("-"*50)
    print("Menu Options")
    print("1. View all students")
    print("2. Add new student")
    print("3. Check eligibility for graduation")
    print("4. Find top performer")
    print("5. Exit")
    print("-"*50)

def main_menu():
    """
    Main interactive menu system
    """
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Please enter a number between 1 and 5")
            continue
        
        match choice:
            case 1:
                # View all students
                print("\n" + "="*50)
                print("List of Students")
                print("="*50)
                for i, name in enumerate(students.keys(), 1):
                    student = students[name]
                    print(f"{i}. {name} (Matric: {student['matric']}, CGPA: {student['cgpa']})")
            
            case 2:
                # Add new student
                add_new_student()
            
            case 3:
                # Check eligibility
                print("\n" + "="*50)
                print("Check Eligibility")
                print("="*50)
                name = input("Enter student name: ")
                eligible, message = check_eligibility(name)
                print("\n" + "-"*30)
                print("Eligibility Result:")
                print("-"*30)
                if eligible:
                    print(f"✓ {message}")
                else:
                    print(f"✗ {message}")
            
            case 4:
                # Find top performer
                print("\n" + "="*50)
                print("Top Performer")
                print("="*50)
                result = find_top_performer()
                if result:
                    name, data = result
                    print(f"Name: {name}")
                    print(f"Matric: {data['matric']}")
                    print(f"Age: {data['age']}")
                    print(f"CGPA: {data['cgpa']}")
                    print(f"Active: {data['is_active']}")
                    print(f"Courses: {data['courses']}")
                    print(f"Grades: {data['grades']}")
            
            case 5:
                # Exit
                print("\nExiting the system...")
                print("Goodbye!")
                break
            
            case _:
                print("Invalid choice. Please enter 1-5")

# Task 4.2:
def check_eligibility(student_name):
    """
    Check if a student is eligible for graduation
    """
    if student_name not in students:
        return False, "Student not found"
    
    student = students[student_name]
    
    # Check conditions using logical operators
    cgpa_ok = student["cgpa"] >= 2.5
    # Check if all courses have grades (no outstanding courses)
    no_outstanding = len(student["courses"]) == len(student["grades"])
    active_ok = student["is_active"]
    
    if cgpa_ok and no_outstanding and active_ok:
        return True, f"{student_name} is eligible for graduation"
    else:
        reasons = []
        if not cgpa_ok:
            reasons.append(f"CGPA ({student['cgpa']}) below 2.5")
        if not no_outstanding:
            reasons.append("has outstanding courses")
        if not active_ok:
            reasons.append("not active")
        return False, f"{student_name} is not eligible: " + ", ".join(reasons)

def find_top_performer():
    """
    Find student with highest CGPA
    """
    if not students:
        return None
    
    top_student = max(students.items(), key=lambda x: x[1]["cgpa"])
    return top_student

def add_new_student():
    """
    Add a new student to the system
    """
    print("\n" + "="*50)
    print("Add New Student")
    print("="*50)
    
    name = input("Enter student name: ")
    
    # Check if student already exists
    if name in students:
        print(f"Student {name} already exists!")
        return
    
    matric = input("Enter matric number: ")
    
    # Get age and CGPA with validation
    age, cgpa = get_valid_input()
    if age is None or cgpa is None:
        print("Failed to add student. Invalid input.")
        return
    
    # Get active status
    active_input = input("Is the student active (yes/no): ").lower()
    is_active = active_input in ["yes", "y", "true"]
    
    # Get courses
    courses_input = input("Enter courses (comma separated): ")
    courses = [course.strip() for course in courses_input.split(",")]
    
    # Add to students dictionary
    students[name] = {
        "matric": matric,
        "age": age,
        "cgpa": cgpa,
        "is_active": is_active,
        "courses": courses,
        "grades": {}  # Empty grades for new student
    }
    
    print(f"\nStudent {name} added successfully!")


# PART 5: ADVANCED CHALLENGES (OPTIONAL)

# Task 5.1:
def process_nested_data():
    """
    Process nested student data (Optional Task 5.1)
    """
    print("\n" + "="*50)
    print("Nested Data Processing")
    print("="*50)
    
    # Create a sample nested dictionary with scores
    student_scores = {
        "Student1": {"Math": 85, "Science": 90, "English": 78},
        "Student2": {"Math": 72, "Science": 88, "English": 91},
        "Student3": {"Math": 95, "Science": 89, "English": 84}
    }
    
    # Calculate average for each student
    for student, scores in student_scores.items():
        avg_score = sum(scores.values()) / len(scores)
        print(f"{student}: Average score = {avg_score:.2f}")
        
        # Check if all scores above 70
        if all(score > 70 for score in scores.values()):
            print(f"  ✓ {student} scored above 70 in all courses")

# Task 5.2:
def detect_type(data):
    """
    Detect and return type of input data (Optional Task 5.2)
    """
    match data:
        case int():
            return f"Integer: {data} (type: int)"
        case float():
            return f"Float: {data} (type: float)"
        case list():
            return f"List: {data} (length: {len(data)})"
        case dict():
            return f"Dictionary: {data} (keys: {list(data.keys())})"
        case str():
            return f"String: '{data}' (length: {len(data)})"
        case _:
            return f"Unknown type: {type(data)}"

# MAIN EXECUTION

if __name__ == "__main__":
    print("="*50)
    print("GSE301 Data Science Project")
    print("Student Academic Performance Analysis System")
    print("="*50)
    
    # Demonstrate Part 3 operations
    demonstrate_slicing()
    demonstrate_set_operations()
    
    # Optional: Uncomment to run advanced challenges
    # process_nested_data()
    # print(detect_type([1, 2, 3]))
    
    # Run the main menu
    main_menu()   