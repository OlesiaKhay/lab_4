# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    import csv
    import json
    with open("input.csv", 'r') as file:
        data = list(csv.reader(file, delimiter= ','))
    keys = data[0]
    res = []
    for elem in data[1:]:
        prom = {}
        for i, key in enumerate(keys):
            prom.update({key: elem[i]})
        res.append(prom)
    return json.dumps(res, indent= 4, separators=(',', ': '))
    ...  # TODO Сериализовать в файл с отступами равными 4

print(task(), end = "")
if __name__ == '__main__':
    # Нужно для проверки
    task()

#    with open(OUTPUT_FILENAME) as output_f:
#        for line in output_f:
#            print(line, end="")
