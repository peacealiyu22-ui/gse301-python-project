# GSE301 Python Project

## Student Academic Performance Analysis System

### Project Overview
A Python-based system for storing, processing, and analyzing mock academic data for a department. This project illustrates basic concepts in programming using Python to create a meaningful application in academic management.

### Features
- Student profile management
- Grade calculation and feedback
- Eligibility checking for graduation
- Set operations for student analysis
- Interactive console menu system
- Error handling and input validation

### Requirements
- Python 3.10 or higher (for match-case support)

### How to Run
1. Clone this repository or download the script
2. Open terminal/command prompt in the project directory
3. Run the command: `python student_analysis.py`
4. Follow the menu prompts to use the system

### Project Structure
- `student_analysis.py` - Main Python script
- `README.md` - This documentation file
- `screenshots/` - Folder for output screenshots


### Python Concepts Demonstrated
1. **Data Types and Variables**: Strings, integers, floats, booleans
2. **Data Structures**: Lists, tuples, dictionaries, sets
3. **Control Flow**: if-elif-else, match-case, loops
4. **Functions**: Custom function definitions and calls
5. **Error Handling**: Try-except blocks
6. **List Operations**: Slicing, indexing, manipulation
7. **Set Operations**: Union, intersection, difference
8. **Type Conversion and Validation**: Input handling
9. **Logical Operators**: and, or for eligibility checks

### Code Organization
The project is organized into five parts as per the requirements:

1. **Part 1**: Data Collection and Storage
   - Variable declaration with different data types
   - Implementation of list, dictionary, set, and tuple
   - Department information storage

2. **Part 2**: Data Processing and Logic
   - Grade calculation using conditional statements
   - Input validation with error handling
   - Match-case for feedback generation

3. **Part 3**: Analysis and Reporting
   - List slicing operations (top scores, last scores, step slicing)
   - Set operations (union, intersection, difference)

4. **Part 4**: Interactive Menu System
   - Console-based menu with match-case
   - Student eligibility checker with logical operators
   - Add new student functionality

5. **Part 5**: Advanced Challenges (Optional)
   - Nested data processing
   - Data type detection using match-case

### Sample Students Included
The system comes pre-loaded with 6 sample student profiles:
1. Aliyu Peace (Matric: 22/40IA017, CGPA: 4.98)
2. Okpala Isaac (Matric: 21/55DZ059, CGPA: 5.0)
3. Adeoye Kehinde (Matric: 22/70DZ093, CGPA: 3.45)
4. Oyedele Yusuf (Matric: 21/55DZ032, CGPA: 2.4)
5. Ekieye Bibian (Matric: 22/70XY066, CGPA: 3.8)
6. Jagaba Shamu (Matric: 24/90FD089, CGPA: 4.2)

### Menu Options
1. **View all students** - Display all student names with matric numbers and CGPA
2. **Add new student** - Interactive form to add a new student with validation
3. **Check eligibility** - Check if a student meets graduation requirements
4. **Find top performer** - Display student with highest CGPA
5. **Exit** - Close the application

### Eligibility Criteria
A student is eligible for graduation if:
- CGPA is 2.5 or above
- All registered courses have grades (no outstanding courses)
- Student is currently active

### Author
**Name:** Aliyu Peace  
**Matric Number:** 22/40IA017  
**Course:** GSE301: Graduates self employment
**Institution:** University of Ilorin

### Submission Details
This project was submitted as part of the GSE301 graduates self employment requirements. The complete code and documentation are available on GitHub.

### Acknowledgments
- University of Ilorin for the learning opportunity
- Course instructors for guidance
- Python documentation and community resources
