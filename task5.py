import json


with open("students.json", "r", encoding="utf-8") as file:
    student_list = json.load(file)

best_student = {"name": "", "age": 0, "score": 0}

for record in student_list:
    record["passed"] = record["score"] >= 60
    best_student = max(best_student, record, key=lambda s: s["score"])

print(f"Студент с максимальным баллом: {best_student['name']} ({best_student['score']})")

with open("students_passed.json", "w", encoding="utf-8") as file:
    json.dump(student_list, file, ensure_ascii=False, indent=4)
