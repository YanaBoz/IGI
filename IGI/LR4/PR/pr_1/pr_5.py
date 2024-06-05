import numpy as np

def task5():
# Создание целочисленной матрицы A[n, m]
 n = 5
 m = 4
 A = np.random.randint(0, 10, size=(n, m))  # Генерация случайных чисел от 0 до 9

# Вывод матрицы
 print("Матрица A:")
 print(A)

# a) Библиотека NumPy:
# 1. Создание массива:
#    - array():
 B = np.array([1, 2, 3, 4, 5])
 print("\nArray B (from list):")
 print(B)
#    - values():
 C = np.array(range(1, 6))
 print("\Array C (with range):")
 print(C)

# 2. Функции создания массива заданного вида:
#    - zeros():
 D = np.zeros((3, 3))
 print("\nMatrice D (zero):")
 print(D)
#    - ones():
 E = np.ones((2, 2))
 print("\nMatrice E (one):")
 print(E)
#    - eye():
 F = np.eye(3)
 print("\nMatrice F (one):")
 print(F)

# 3. Индексирование массивов NumPy:
#    - Индекс:
 print("\nElement A[1, 2]:")
 print(A[1, 2])  # Вывод элемента на пересечении 2-й строки и 3-го столбца
#    - Срез:
 print("\nSrez A[1:3, :]:")
 print(A[1:3, :])  # Вывод элементов со 2-й по 3-ю строки, всех столбцов

# 4. Операции с массивами:
#    - Универсальные (поэлементные) функции:
 print("\nMatrice A * 2:")
 print(A * 2)  # Умножение каждого элемента на 2
 print("\nMatrice A + 5:")
 print(A + 5)  # Прибавление 5 к каждому элементу

# b) Математические и статистические операции:
# 1. mean():
 mean_A = np.mean(A)
 print("\nSr_arifm A:")
 print(mean_A)

# 2. median():
 median_A = np.median(A)
 print("\nMediane A:")
 print(median_A)

# 3. corrcoef():
 print("\nKorel A:")
 print(np.corrcoef(A))

# 4. var():
 variance_A = np.var(A)
 print("\nDisp A:")
 print(variance_A)

# 5. std():
 stddev_A = np.std(A)
 print("\nOtkl A:")
 print(stddev_A)

# Подсчет элементов, превосходящих среднее значение:
 count_above_mean = np.sum(A > mean_A)
 print("\nabove average:")
 print(count_above_mean)

# Вычисление стандартного отклонения для элементов, превосходящих среднее:
 above_mean_values = A[A > mean_A]
 stddev_above_mean_func = np.std(above_mean_values)  # С использованием функции
 print("\nstddev_above_mean_func:")
 print(round(stddev_above_mean_func, 2))  # Округление до сотых

    # Вычисление стандартного отклонения через формулу:
 stddev_above_mean_formula = np.sqrt(np.sum((above_mean_values - np.mean(above_mean_values)) ** 2) / (count_above_mean - 1))
 print("\nstddev_above_mean_func:")
 print(round(stddev_above_mean_formula, 2))

if __name__ == "__main__":
    task5()