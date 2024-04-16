from scipy.stats import chi2
from math import exp, factorial
from numpy.random import randint
from numpy import sort, diff, append, array

def count_duplicates(numbers):
    occurrences_count = {}
    for num in numbers:
        if num in occurrences_count:
            occurrences_count[num] += 1
        else:
            occurrences_count[num] = 1
    
    counts_nums = {}
    for num, count in occurrences_count.items():
        if count - 1 in counts_nums:
            counts_nums[count - 1] += 1
        else:
            counts_nums[count - 1] = 1

    result = [0] * max(occurrences_count.values())
    for count, num in counts_nums.items():
        result[count] = num

    return result

# Пример использования
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6,6,6,6,6,7,7]
# print(count_duplicates(numbers))  # Вывод: [1, 2, 2, 1, 1]

def perform_birthday_spacing_test(numbers, n, m, high):
    sorted_nums = sort(numbers)
    # print(sorted_nums)
    spacings = append(diff(sorted_nums), sorted_nums[0] - sorted_nums[-1] + high)
    # print(spacings)
    duplicates = count_duplicates(spacings)
    print(duplicates)
    k = len(duplicates)

    l = n**3 / (4 * high)
    print(l)
    mult = exp(-l)

    s = 0
    p_last = 1
    for i in range(k):
        p = l**i * mult / factorial(i)
        # print("p =", p)
        p_last -= p
        # print((duplicates[i] - p * n)**2 / p / n)
        # print(duplicates[i], p)
        s += (duplicates[i] - p * n)**2 / p / n
    # print(p_last * n)
    s += p_last * n
    # print("p_last =", p_last)

    return s


# n = 2**21
# m = 63 # max
n = 4
m = 4
high=2**m
random_points = randint(low=0.0, high=high, size=n)
if n < 20:
    print(random_points)
chi = perform_birthday_spacing_test(random_points, n, m, high)
print(chi)
# print(perform_birthday_spacing_test(array([12,3,4,5]), 4, 4, 16))

from scipy import stats
print(1 - stats.chi2.cdf(chi, 2))
