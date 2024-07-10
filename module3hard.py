# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)
def calculateStructureSum(dataStructure):
    """Вычисление суммы любой структуры данных"""
    date = dataStructure
    global count
    for x in date:
        if isinstance(x, int):
            count = count + x
        elif isinstance(x, str):
            count = count + len(x)
        elif isinstance(x, dict):
            calculateStructureSum(x.keys())
            calculateStructureSum(x.values())
        else:
            calculateStructureSum(x)
            continue


dataStructure = [[1, 2], [4, 5], 'aaa', {1 : 2}]
dataStructure1 = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
count = 0

calculateStructureSum(dataStructure1)
print(count)
print(help(calculateStructureSum))




