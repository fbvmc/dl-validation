import csv
import numpy

numbersList = []

with open('population-completeness.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} Wikidata link with name: {row[1]} .')

            if not row[1].startswith("Q"):
                numbersList.append(row[1])
            line_count += 1
    print(f'Processed {line_count} lines.')

    random_num = numpy.random.choice(numbersList, 100);
    print(random_num)

    with open('random-names.txt', 'w') as f:
        for item in random_num:
            f.write("%s\n" % item)