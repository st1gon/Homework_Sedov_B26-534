from task1_3 import create_chess_matrix
from task2_3 import longest_series
from task3_3 import top_three_chars
from task4_3 import rotate_matrix_clockwise
from task5_3 import find_anomalies_pure
from task6_3 import generate_sales_file, analyze_sales
from task7_3 import find_most_similar_strings
from task8_3 import retry
from task9_3 import Store, Book, Electronic
from task10_3 import TaskManager, Task

def main():
    print("=== Выполнение всех задач Варианта 3 ===\n")

    print("--- Задача 1 ---")
    print(create_chess_matrix(3, 3))

    print("\n--- Задача 2 ---")
    print(longest_series([1, 1, 1, 2, 2, 3, 3, 3, 3]))

    print("\n--- Задача 3 ---")
    print(top_three_chars("Python Programming"))

    print("\n--- Задача 4 ---")
    print(rotate_matrix_clockwise([[1, 2], [3, 4]]))

    print("\n--- Задача 5 ---")
    print(find_anomalies_pure([10, 12, 11, 100, 9]))

    print("\n--- Задача 6 ---")
    generate_sales_file("sales_data.csv", 100)
    analyze_sales("sales_data.csv")

    print("\n--- Задача 7 ---")
    print(find_most_similar_strings(["abcdef", "abcxef"]))

    print("\n--- Задача 8 ---")
    @retry(2)
    def test_func():
        return "Успешно"
    print(test_func())

    print("\n--- Задача 9 ---")
    s = Store()
    s.add_product(Book("Book", 500, 5, "Author"))
    s.sell_product("Book", 1)

    print("\n--- Задача 10 ---")
    tm = TaskManager()
    tm.add_task(Task("Task 1", "High", "Pending", "2026-10-01"))
    print(tm.get_high_priority_tasks())

if __name__ == "__main__":
    main()
