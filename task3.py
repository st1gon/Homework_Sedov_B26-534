import csv

class Group:
    __students_counter: int
    __score_sum: int

    def __init__(self):
        self.__students_counter = 0
        self.__score_sum = 0

    def add_score(self, score: int):
        self.__score_sum += score

    def increment(self):
        self.__students_counter += 1

    def get_mean(self):
        return self.__score_sum / self.__students_counter



with open("students.csv") as file:
    reader = csv.DictReader(file)
    class_summary: Group = Group()
    top_student: tuple[str, int] = ("Name", 0)
    group_stats: dict[str, Group] = dict()
    for student_row in reader:
        class_summary.increment()
        class_summary.add_score(int(student_row["score"]))
        if top_student[1] < int(student_row["score"]):
            top_student = (student_row["name"], int(student_row["score"]))
        if student_row["group"] not in group_stats:
            group_stats[student_row["group"]] = Group()
        group_stats[student_row["group"]].add_score(int(student_row["score"]))
        group_stats[student_row["group"]].increment()

    print(f"mean = {class_summary.get_mean()}")
    print(f"max score = {top_student}")
    for group_name, group_summary in group_stats.items():
        print(f"{group_name} - {group_summary.get_mean()}")

