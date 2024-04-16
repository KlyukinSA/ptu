from scipy.stats import norm

P = 0.99  # Уровень для квантиля

quantile = norm.ppf(P)  # Вычисляем квантиль

print("t_a =", quantile)
