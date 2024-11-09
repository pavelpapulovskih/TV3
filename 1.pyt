import math
data = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70,
75, 65, 84, 90, 150]
n = len(data)
# Среднее арифметическое
mean = sum(data) / n
# Смещенная дисперсия
variance_biased = sum((x - mean) ** 2 for x in data) / n
# Несмещенная дисперсия
variance_unbiased = sum((x - mean) ** 2 for x in data) / (n - 1)
# Среднее квадратичное отклонение
stddev = math.sqrt(variance_biased)
print(f"Среднее арифметическое: {mean:.2f}")
print(f"Среднее квадратичное отклонение: {stddev:.2f}")
print(f"Смещенная дисперсия: {variance_biased:.2f}")
print(f"Несмещенная дисперсия: {variance_unbiased:.2f}")
