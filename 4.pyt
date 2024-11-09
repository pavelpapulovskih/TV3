# Вероятности сдачи сессии
pA = 0.8
pB = 0.7
pC = 0.9
# Пропорции студентов
total_students = 2 + 2 + 4 # факультет C имеет в два раза большестудентов, чем A и B вместе
prob_A = 2 / total_students
prob_B = 2 / total_students
prob_C = 4 / total_students
# Вероятности сдачи сессии для факультетов
prob_pass_A = prob_A * pA
prob_pass_B = prob_B * pB
prob_pass_C = prob_C * pC
# Общая вероятность сдачи сессии
total_prob = prob_pass_A + prob_pass_B + prob_pass_C
# Вероятности для каждого факультета
prob_A_given_pass = prob_pass_A / total_prob
prob_B_given_pass = prob_pass_B / total_prob
prob_C_given_pass = prob_pass_C / total_prob
print(f"Вероятность, что студент учится на факультете A:{prob_A_given_pass:.5f}")
print(f"Вероятность, что студент учится на факультете B:{prob_B_given_pass:.5f}")
print(f"Вероятность, что студент учится на факультете C:{prob_C_given_pass:.5f}")