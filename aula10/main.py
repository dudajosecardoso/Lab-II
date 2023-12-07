def calculate_average(grades):
    grades_list = [int(grade) for grade in grades.split()]
    return sum(grades_list) / len(grades_list)

def process_students_grades(names_file, grades_file):
    students_names = names_file.readlines()
    students_grades = grades_file.readlines()

    for i in range(len(students_names)):
        current_grades = students_grades[i].split()
        total_sum = sum(int(grade) for grade in current_grades)
        average = total_sum / len(current_grades)

        print(f"{students_names[i].strip()}: Soma = {total_sum}, Média = {average:.2f}")

def main():
    names_file = open("students_names.txt", 'r')
    grades_file = open("students_grades.txt", 'r')

    process_students_grades(names_file, grades_file)

    names_file.close()
    grades_file.close()
main()
