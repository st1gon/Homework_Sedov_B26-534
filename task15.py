from io import StringIO


def count_lines(input_stream):
    return sum(1 for _ in input_stream)


if __name__ == "__main__":
    print(count_lines(StringIO("first\nsecond\nthird")))
    with open("task1.txt", encoding="utf-8") as source_file:
        print(count_lines(source_file))
