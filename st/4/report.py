M = 1 # бит
T = 1 # секунд за бит
ks = [4, 11, 7, 5, 26, 21, 16, 11, 6, 57, 51, 45, 39, 36, 30, 24, 18]
ks = [ks[index] for index in [0, 1,2,3, 4,5,6, 9,10,11]]
prob_thresh = 1e-5
result_path = 'full/full_result2с.csv' # ','-separated. ';' not work
separator = ','


def get_prob(tokens):
	return float(tokens[-2].replace('"', '')) / float(tokens[-1].replace('"', ''))
print('table 1')
file = open(result_path, 'r')
prev = True
fzs = []
pn = '-1'
t2 = []
for i, line in enumerate(file):
	tokens = line.split(separator)
	p = get_prob(tokens)
	gave_few_errors = p <= prob_thresh
	prob_view = "%0.1e" % p
	if gave_few_errors:
		prob_view = '"p <= ' + str(prob_thresh) + '"'
	k = ks[i % len(ks)]
	print(line[:-1], prob_view, k, sep=separator)
	cn = tokens[0].replace('"', '')
	if cn != pn and gave_few_errors:
		pn = cn
		fzs.append((tokens, k))
		t2.append((tokens[1].replace('"', ''), int(cn), k))

print('table 2')
for p, n, k in t2:
	h = n - k
	print(p, n, h, sep=separator)


def get_code_redundancy(n, k):
	return (n - k) / n

def get_file_transfer_time(n, k, N_c, N):
	return (M / k) * n * T * N / N_c

print('table 3')
a = []
for tokens, k in fzs:
	p = tokens[1].replace('"', '')
	n = int(tokens[0].replace('"', ''))
	N_c = int(tokens[3].replace('"', ''))
	N = int(tokens[-1].replace('"', ''))
	
	r = get_code_redundancy(n, k)
	t = get_file_transfer_time(n, k, N_c, N)
	line = (p, n, k, r, t)
	print(*line, sep=separator)
	a.append(line)

print('table 4')
p = -1
ps = []
for l in a:
	if l[0] != p:
		p = l[0]
		ps.append(p)
for p in ps:
	b = list(filter(lambda l: l[0]==p, a))
	for pos, name in (-2, "A"), (-1, "B"):
		res = min(b, key=lambda l: l[pos])
		print(res[0], name, *res[1:], sep=separator)
