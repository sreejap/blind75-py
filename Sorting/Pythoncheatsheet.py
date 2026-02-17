arr.sort()                 # in-place ascending
arr.sort(reverse=True)     # descending
sorted(arr)                # returns new sorted list

# custom key
arr.sort(key=lambda x: x[1])

In Python, you can use list.sort() to sort the content of the list in-place, or sorted(list) to return a new list containing the sorted list. They are both stable sorts. Python uses Timsort, which uses merge sort for larger data and insertion sort for smaller data.

# Custom sorting
Custom Sorting in Python
In Python, you can use list.sort() to sort the content of the list in-place and sorted(list) to return a new list containing the sorted list. By default, both sorting functions sort a list in ascending order. Optionally, they can take 2 extra parameters, reverse and key to change the default sorting order.

list.sort(reverse = True|False, key = comp_function)

reverse = True will sort the list in descending order
key is a function that specifies the sorting order
words = ["zebra", "fat", "apple", "lion", "ink"]
# sort words alphabetically
words.sort()    # words = ["apple", "fat", "ink", "lion", "zebra"]

nums = [40, 100, 1, 5, 25, 10]
# sort nums in ascending order
nums.sort()     # nums = [1, 5, 10, 25, 40, 100]
# sort nums in descending order
nums.sort(reverse=True)      # nums = [100, 40, 25, 10, 5, 1]

# task tuples (description, priority)
tasks = [
    ('Cook dinner', 5),
    ('Buy grocery', 3)
]

# sort tasks by priority in ascending order
sorted_tasks = sorted(tasks, key=lambda task: task[1])
# or use cmp_to_key
sorted_tasks = sorted(tasks, key=cmp_to_key(lambda t1, t2: t1[1] - t2[1]))
# sorted_tasks = [('Buy grocery', 3), ('Cook dinner', 5)]


# Example for custom comparator
class Student:
    def __init__(self, name: str, math_grade: int, english_grade: int) -> None:
        self.name = name
        self.math_grade = math_grade
        self.english_grade = english_grade

    def get_total_grade(self) -> int:
        return self.math_grade + self.english_grade

def print_student_names(students: list[Student]) -> None:
    print(" ".join(s.name for s in students))

def print_sorted_students(students: list[Student]) -> None:
    # sort students by their total grade in ascending order
    students.sort(key=lambda student:student.get_total_grade())
    print_student_names(students)
    # sort students by their total grade in descending order
    students.sort(reverse=True, key=lambda student:student.get_total_grade())
    print_student_names(students)

if __name__ == "__main__":
    students = []
    for _ in range(int(input())):
        line = input().split()
        students.append(Student(line[0], int(line[1]), int(line[2])))
    print_sorted_students(students)

