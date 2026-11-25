import json


def load_students():
    try:
        file = open("students.json", "r", encoding="utf-8")
        students = json.load(file)
        file.close()
        return students

    except FileNotFoundError as e:
        print("File Error:", e)
        return []

    except json.JSONDecodeError as e:
        print("JSON Error:", e)
        return []


def save_students(students):
    try:
        file = open("students.json", "w", encoding="utf-8")
        json.dump(students, file, indent=4)
        file.close()

    except Exception as e:
        print("Error:", e)

    except Exception as e :
        print("ERROR: ", e)


def show_students():

    try:
        students = load_students()

        if not students:
            print("student list is empty")
            return

        for student in students:
            print("-----------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])

    except Exception as e:
        print("error:", e)

def update_student():

    try:
        students = load_students()

        student_id = int(input("enter student ID: "))

        for student in students:

            if student["id"] == student_id:
                student["name"] = input("enter new name: ")
                student["age"] = int(input("enter new age: "))

                save_students(students)
                print("student updated")
                return

        print("student not found")

    except ValueError as e:
        print("value Error:", e)

    except Exception as e:
        print("error:", e)

def delete_student():

    try:
        students = load_students()

        student_id = int(input("enter student ID: "))

        for student in students:

            if student["id"] == student_id:
                students.remove(student)
                save_students(students)

                print("student deleted")
                return

        print("student not found")

    except ValueError as e:
        print("value Error:", e)

    except Exception as e:
        print("error:", e)


def search_student():

    try:
        students = load_students()

        student_id = int(input("enter student ID: "))

        for student in students:

            if student["id"] == student_id:
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                return

        print("student not found")

    except ValueError as e:
        print("value Error:", e)

    except Exception as e:
        print("error:", e)