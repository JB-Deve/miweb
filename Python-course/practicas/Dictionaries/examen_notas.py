# pesado
import os
os.system("cls")
"""
The code in examGrades.py checks student answers to an exam quiz against model answers and
outputs how many correct answers each student achieved.
Modify the code in this program to include following:
a. refactor the script into a function, get_grades(),which returns a dictionary containing
the grade (number of correct answers) achieved per student;
b. write a new function, sorted_by_grade(), which displays students in ascending order of
the grade they achieved; and
c. write a new function, main(), which simply calls the functions you defined in a and b above.
"""

student_answers = {
"Adam": ['A', 'B', 'A', 'C', 'C', 'D', 'A', 'D', 'A', 'E'],
"Bob":  ['D', 'B', 'A', 'B', 'C', 'A', 'C', 'D', 'A', 'E'],
"Carol":['A', 'C', 'D', 'A', 'C', 'B', 'C', 'D', 'A', 'E'],
"Jon":  ['C', 'B', 'A', 'E', 'D', 'C', 'A', 'D', 'A', 'E'],
"Liz":  ['A', 'B', 'A', 'C', 'A', 'E', 'D', 'E', 'A', 'E'],
"Marc": ['A', 'C', 'D', 'C', 'C', 'D', 'A', 'D', 'A', 'E'],
"Mia":  ['B', 'B', 'E', 'C', 'A', 'D', 'A', 'D', 'A', 'E'],
"Zia":  ['E', 'B', 'E', 'C', 'A', 'E', 'C', 'E', 'A', 'E']
}

# Key to the questions
model_answers = ['A', 'C', 'D', 'C', 'A', 'D', 'A', 'D', 'A', 'E']

# A
def get_grades(student_answers, model_answers):
    std_answers = {}
    
    for name, answers in student_answers.items():
        contador = 0

        for i in range(len(answers)):
            if answers[i] == model_answers[i]:
                contador += 1
        std_answers[name] = contador
    return std_answers
    
# B sortby grade en acending order by grade

def sort_by_grade(student_answers):
    
    students = sorted((values, key) for (key, values) in student_answers.items())
    # students = students[::-1] # inversor the listas 
    students = dict((key, values) for (values, key) in students)
    
    for student in students:
        print(f"{student:5} achieved: {students[student]} correct answers.")


# C
def main():
    # resultado = get_grades(student_answers, model_answers)
    # print(resultado)
    title = "==== Student's list ===="
    print(f"{title.center(len(title) + 10)}\n")
    sort_by_grade(get_grades(student_answers, model_answers))

main()
