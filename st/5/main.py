n=[7,15,15,15,31,31,31,63,63]
k=[4,11,7,5,26,21,16,57,51]


def tones(we, woe):
  for i in range(len(n)):
    print(n[i], k[i], we[i], woe, '%0.2f' % (float(we[i])/woe), sep=',')


print(0.003)
tones([400,556,336,235,631,513,386,684,613], 759)
print(0.001)
tones([507,665,417,290,764,617,474,824,742], 914)
print(0.0005)
tones([542,704,445,318,804,651,498,870,782], 962)