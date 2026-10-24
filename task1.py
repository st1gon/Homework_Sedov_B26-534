with open("task1.txt", "r") as file:
    file_text = file.read()
    print(len(file_text.split("\n")))
    print(len(file_text.split()))
    print(len(file_text))
    print(max(file_text.split("\n")))
