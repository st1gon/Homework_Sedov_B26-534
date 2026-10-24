import csv


with open("product.csv", "r") as file:
    reader = csv.DictReader(file)


    with open("expensive.csv", "w") as filtered_file:
        writer = csv.DictWriter(filtered_file, reader.fieldnames)
        writer.writeheader()
        for item in reader:
            if int(item["price"]) > 100:
                writer.writerow(item)

