from math import log10, sqrt
from scipy.stats import norm

Pt = 43 # по условию
print('модель потерь 3G для пешеходной среды ')
ds = [0.259, 0.248, 0.255] # километры
f = 2137 # мегагерц
s = 0
for d in ds:
    PL = int(40*log10(d) + 30*log10(f) + 49)
    print('PL = 40lg(', d, ') + 30lg(', f, ') + 49 = ', PL, sep='')
    Pr = Pt - PL
    print('Pr = ', Pt, ' - ', PL, ' = ', Pr, sep='')
    s += Pr
mean_3g = int(s / len(ds))

print('определение 3D расстояний от базовой станции до терминала пешехода')
d2Ds = [284, 276, 279] # метры
d3Ds = [] # метры
nfl = 3 # этаж
hUT = 3*(nfl - 1) + 1.5 # метры
print('hUT = 3*(', nfl, ' - 1) + 1.5 = ', hUT, sep='')
hBS = 25 # метры, типовое
for d2D in d2Ds:
    d = int(sqrt(d2D**2 + (hBS - hUT)**2))
    print('d3D = sqrt(', d2D, '**2 + (', hBS, ' - ', hUT, ')**2) = ', d, sep='')
    d3Ds.append(d)

print('модель потерь 4G для макросот и отсутствии прямой видимости и внутри помещения')
h = 20 # метры, типовое
W = 20 # метры, типовое
# f = 2630 # МГц
f = 2.63 # ГГц
PLtw = 20 # затухание сигнала в стенах
d2Din = 8 # метры
s = 0
for d3D in d3Ds:
    PL = int(161.04 - 7.1*log10(W) + 7.5*log10(h) - (24.37 - 3.7*(h / hBS)**2)*log10(hBS) + (43.42 - 3.1*log10(hBS))*(log10(d3D) - 3) + 20*log10(f) - (3.2*(log10(17.625))**2 - 4.97) - 0.6*(hUT - 1.5))
    print('PL = 161.04 - 7.1lg(', W, ') + 7.5lg(', h, ') - (24.37 - 3.7*(', h, ' / ', hBS, ')**2)lg(', hBS, ') + (43.42 - 3.1lg(', hBS, '))*(lg(', d3D, ') - 3) + 20*lg(', f, ') - (3.2*(lg(17.625))**2 - 4.97) - 0.6*(', hUT, ' - 1.5) = ', PL, sep='')
    PL2 = PL + PLtw + 0.5 * d2Din
    print('PL_помещ = ', PL, ' + ', PLtw, ' + ', 0.5 * d2Din, ' = ', PL2, sep='')
    Pr = Pt - PL2
    print('Pr = ', Pt, ' - ', PL2, ' = ', Pr, sep='')
    s += Pr
mean_4g = int(s / len(d2Ds))

print('определение вероятности нахождения телефона в зоне уверенного приема')
print('среднее 3g =', mean_3g)
print('среднее 4g =', mean_4g)
std_dev_3g = 12
std_dev_4g = 6
print('ско 3g внутри помещения =', std_dev_3g)
print('ско 4g для NLOS =', std_dev_4g)
threshold = -100
def prob(mean, std):
    return int(100 * (1 - norm.cdf(threshold, mean, std))) / 100
# probability_3g = 1 - norm.cdf(threshold, mean_3g, std_dev_3g)
probability_3g = prob(mean_3g, std_dev_3g)
print('вероятность для 3g = 1 - norm.cdf(', threshold, ', ', mean_3g, ', ', std_dev_3g, ') = ', probability_3g, sep='')
# probability_4g = 1 - norm.cdf(threshold, mean_4g, std_dev_4g)
probability_4g = prob(mean_4g, std_dev_4g)
print('вероятность для 4g = 1 - norm.cdf(', threshold, ', ', mean_4g, ', ', std_dev_4g, ') = ', probability_4g, sep='')
