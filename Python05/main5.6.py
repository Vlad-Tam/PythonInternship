students = [
    {
        'firstname': 'Masha',
        'Group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 8,
    },
    {
        'firstname': 'Vlad',
        'Group': 1,
        'physics': 4,
        'informatics': 9,
        'history': 5
    },
    {
        'firstname': 'Petr',
        'Group': 2,
        'physics': 5,
        'informatics': 4,
        'history': 3
    },
    {
        'firstname': 'Anna',
        'Group': 3,
        'physics': 2,
        'informatics': 8,
        'history': 1
    },
    {
        'firstname': 'Ivan',
        'Group': 4,
        'physics': 4,
        'informatics': 5,
        'history': 2
    }
]


def find_smart_students(students_list: list) -> list:
    smart_students_info = []
    for student in students_list:
        total_score = 0
        for key, value in student.items():
            if (key != 'firstname') & (key != 'Group'):
                total_score += value
        if total_score / (len(student) - 2) > 4:
            smart_students_info.append(student)
    return smart_students_info


def find_average_subject_score(students_list: list, subject_name: str) -> float:
    total_score = 0
    for student in students_list:
        for key, value in student.items():
            if key == subject_name:
                total_score += value
    return total_score / len(students_list)


def main():
    print(f'Students with an average grade of more than 4: {find_smart_students(students)}')
    print(f"Physics average grade: {find_average_subject_score(students, subject_name='physics')}")
    print(f"Informatics average grade: {find_average_subject_score(students, subject_name='informatics')}")
    print(f"History average grade: {find_average_subject_score(students, subject_name='history')}")


if __name__ == '__main__':
    main()
