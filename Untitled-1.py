def input_students():

    students = []

    num = int(input("Enter number of students: "))


    for i in range(num):
      name = input(f"Enter student {i + 1} name: ")
      score = float(input(f"Enter {name}'s score (0-100): "))
      while score<0 or score>100:
        print("innvalid number, should be from 0 to 100")
        score = float(input(f"Enter a valid score (0-100): "))
      students.append((name, score))

    return students


def print_students(students):
    print("\nAll students and scores:")
    for name, score in students:
        print(f"{name} - {score}")


def average_score(students):
    total = sum(score for _, score in students)
    return total / len(students)


def top_student(students):
    return max(students, key=lambda s: s[1])


def failed_students(students):   
    return [name for name, score in students if score < 60]

def sum_scores_recursive(scores):
    if not scores:
        return 0
    else:
        return scores[0] + sum_scores_recursive(scores[1:])
    
def main():
    print("Welcome to the Student Grade Manager!\n")

    students = input_students()

    print_students(students)

    avg = average_score(students)

    top = top_student(students)

    failed = failed_students(students)

    scores = [score for _, score in students]

    print("\n RESULTS")    
    print(students)
    print(f"Average score: {avg:.2f}")
    print(f"Top student: {top[0]} ({top[1]})")
    print("Failed students:", ", ".join(failed) if failed else "None")
    
    total_recursive = sum_scores_recursive(scores)
    print(f"\n Total (calculated recursively): {total_recursive}")

if __name__ == "__main__":
    main()