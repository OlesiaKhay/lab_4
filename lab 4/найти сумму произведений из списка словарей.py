# TODO решите задачу
def task() -> float:
    import json
    with open ("input.json", "r") as file:
        data = json.load(file)
    res = []
    for elem in data: res.append(elem['score']*elem['weight'])
    return round(sum(res), 3)



print(task())
