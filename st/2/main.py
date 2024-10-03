import matplotlib.pyplot as plt
import numpy as np


seq = [1, 0, 1, 0, 0, 1, 1, 0]
# seq = [1, 0, 1, 1, 0, 1, 1, 0]
# seq = [1, 0, 1, 1, 1, 0, 1, 1]
sample = 30
subs = 6#11
n = len(seq)
x = np.arange(sample * n)

# Нормализуем ось X для диапазона от 0 до 8
x_normalized = 8 * x / (sample * n)

# Генерируем синусоиды
y = np.sin(2 * np.pi * 1.5 * x[0:sample] / sample)
z = np.array([seq[0]] * sample)
state = 1
for i in range(n - 1):
    ny = np.sin(2 * np.pi * 1.5 * x[sample * (i + 1):sample * (i + 2)] / sample)
    if (seq[i + 1] == 0):
        state *= -1
    nz = np.array([seq[i + 1]] * sample)
    y = np.concatenate((y, state * ny), axis=None)
    z = np.concatenate((z, nz), axis=None)

# Создаем графики
plt.subplot(subs, 2, 1)
plt.plot(x_normalized, z)

plt.subplot(subs, 2, 2)
plt.plot(x_normalized, y)
for xc in 8 * np.arange(n) / n:  # Вертикальные линии
    plt.axvline(x=xc, linestyle='--', color='gray')
plt.ylabel('Sk')
plt.yticks([])  # Убираем отображение меток по оси Y

# Создаем новый график синусоиды для нижней части
plt.subplot(subs, 2, 3)
y_lower = np.sin(2 * np.pi * 1.5 * x[0:sample] / sample)
for i in range(n - 1):
    ny_lower = np.sin(2 * np.pi * 1.5 * x[sample * (i + 1):sample * (i + 2)] / sample)
    y_lower = np.concatenate((y_lower, ny_lower), axis=None)

plt.plot(x_normalized, y_lower)
for xc in 8 * np.arange(n) / n:  # Вертикальные линии
    plt.axvline(x=xc, linestyle='--', color='gray')
plt.ylabel('So')
plt.yticks([])  # Убираем отображение меток по оси Y

# Добавляем график -So
plt.subplot(subs, 2, 4)
plt.plot(x_normalized, -y_lower)
for xc in 8 * np.arange(n) / n:  # Вертикальные линии
    plt.axvline(x=xc, linestyle='--', color='gray')
plt.ylabel('-So')
plt.yticks([])  # Убираем отображение меток по оси Y

# Добавляем график So * Sk
plt.subplot(subs, 2, 5)
plt.plot(x_normalized, y * y_lower)
for xc in 8 * np.arange(n) / n:  # Вертикальные линии
    plt.axvline(x=xc, linestyle='--', color='gray')
plt.ylabel('So * Sk')
plt.yticks([])  # Убираем отображение меток по оси Y

# Добавляем график -So * Sk
plt.subplot(subs, 2, 6)
plt.plot(x_normalized, -y_lower * y)
for xc in 8 * np.arange(n) / n:  # Вертикальные линии
    plt.axvline(x=xc, linestyle='--', color='gray')
plt.ylabel('-So * Sk')
plt.yticks([])  # Убираем отображение меток по оси Y

# Новый график для прямых от 0 до 1 или -1 в зависимости от So * Sk
int_vals = []
plt.subplot(subs, 2, 7)
y_product = y * y_lower  # Вычисляем So * Sk
for i in range(n):
    # Получаем значение So * Sk в текущем интервале
    value = y_product[i * sample + sample // 2]  # Получаем значение в середине интервала
    int_vals.append(-value)
    if value > 0:  # Если So * Sk больше 0
        plt.plot([x_normalized[i * sample + sample - 1], x_normalized[i * sample + sample - 1]], [1, 0], color='blue')  # Прямая вверх
        plt.plot([x_normalized[i * sample], x_normalized[i * sample + sample - 1]], [0, 1], color='blue')  # Прямая вправо
    else:  # Если So * Sk меньше или равно 0
        plt.plot([x_normalized[i * sample + sample - 1], x_normalized[i * sample + sample - 1]], [0, -1], color='red')  # Прямая вниз
        plt.plot([x_normalized[i * sample], x_normalized[i * sample + sample - 1]], [0, -1], color='red')  # Прямая вправо

    # Добавляем вертикальные пунктирные линии
    plt.axvline(x=x_normalized[i * sample], linestyle='--', color='gray')

plt.ylabel('int(s0sk)')
plt.yticks([])  # Убираем отображение меток по оси Y
plt.ylim(-1.5, 1.5)  # Ограничиваем диапазон по оси Y

# Новый график для прямых от 0 до 1 или -1 в зависимости от -So * Sk
plt.subplot(subs, 2, 8)
for i in range(n):
    # Получаем значение So * Sk в текущем интервале
    value = y_product[i * sample + sample // 2]  # Получаем значение в середине интервала
    if value < 0:  # Если So * Sk больше 0
        plt.plot([x_normalized[i * sample + sample - 1], x_normalized[i * sample + sample - 1]], [1, 0], color='blue')  # Прямая вверх
        plt.plot([x_normalized[i * sample], x_normalized[i * sample + sample - 1]], [0, 1], color='blue')  # Прямая вправо
    else:  # Если So * Sk меньше или равно 0
        plt.plot([x_normalized[i * sample + sample - 1], x_normalized[i * sample + sample - 1]], [0, -1], color='red')  # Прямая вниз
        plt.plot([x_normalized[i * sample], x_normalized[i * sample + sample - 1]], [0, -1], color='red')  # Прямая вправо

    # Добавляем вертикальные пунктирные линии
    plt.axvline(x=x_normalized[i * sample], linestyle='--', color='gray')

plt.ylabel('int(-s0sk)')
plt.yticks([])  # Убираем отображение меток по оси Y
plt.ylim(-1.5, 1.5)  # Ограничиваем диапазон по оси Y

none_val = 0 #0.5
# z^-1
plt.subplot(subs, 2, 9)
z = 0
zs = []
for i in range(n):
    if i == 0:
        val = none_val
    elif int_vals[i-1] > 0:
        val = 0
    else:
        val = 1
    zs.extend([val] * sample)
plt.plot(x_normalized, zs) 
plt.plot(x_normalized[0:sample], [none_val] * sample, 'r') 
plt.ylabel('z^-1')

# xor
plt.subplot(subs, 2, 10)
z = 0
zs = []
for i in range(n):
    if i == 0:
        val = none_val
    elif int_vals[i-1] > 0:
        val = int(int_vals[i] < 0)
    else:
        val = int(int_vals[i] > 0)
    zs.extend([val] * sample)
plt.plot(x_normalized, zs) 
plt.plot(x_normalized[0:sample], [none_val] * sample, 'r') 
plt.ylabel('xor')

# inv
plt.subplot(subs, 2, 11)
z = 0
zs = []
for i in range(n):
    if i == 0:
        val = none_val
    elif int_vals[i-1] > 0:
        val = int(int_vals[i] > 0)
    else:
        val = int(int_vals[i] < 0)
    zs.extend([val] * sample)
plt.plot(x_normalized, zs) 
plt.plot(x_normalized[0:sample], [none_val] * sample, 'r') 
plt.ylabel('inv')

# Показываем графики
plt.tight_layout()
plt.show()
