import random


sample_size = 5
rockyou_path = 'rockyou.txt'
rockyou_lines_count = 14344391
if False:
  rockyou_path = 'test-rockyou.txt'
  rockyou_lines_count = 6

s = random.sample(range(0, rockyou_lines_count), sample_size)
s.sort()

f = open(rockyou_path, 'rb')
i = 0
for line in f:
  if len(s) < 1:
    break
  if i == s[0]:
    s.pop(0)
    print(line.decode("utf-8"), end='')
  i += 1
