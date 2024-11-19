M = 1 # бит
T = 1 # секунд за бит
ks = [4, 11, 7, 5, 26, 21, 16, 11, 6, 57, 51, 45, 39, 36, 30, 24, 18]
remain_data_lines_count = 14

result_path = 'resultc.csv' # ';' not work
separator = ','
def has_few_errors(tokens, p):
	# return tokens[-2] == '"0"' or tokens[-2] == '"1"'
	return p <= 1e-6


def get_prob(tokens):
	return float(tokens[-2].replace('"', '')) / float(tokens[-1].replace('"', ''))

print('table 1')
def print_table1_row(line, p):
	print(line[:-1] + separator + "%0.1e" % p)
file = open(result_path, 'r')
prev = True
fzs = []
for i, line in enumerate(file):
	tokens = line.split(separator)
	p = get_prob(tokens)
	zero = has_few_errors(tokens, p)
	if zero and prev:
		print_table1_row(line, p)
		fzs.append((tokens, i))
		prev = False
	if not zero and not prev:
		prev = True
	if prev:
		print_table1_row(line, p)

def get_code_redundancy(n, k):
	return (n - k) / n

def get_file_transfer_time(n, k, N_c, N):
	return (M / k) * n * T * N / N_c

print('table 2')
a = []
for tokens, i in fzs:
	p = tokens[1].replace('"', '')
	n = int(tokens[0].replace('"', ''))
	k = ks[i % remain_data_lines_count]

	N_c = int(tokens[3].replace('"', ''))
	N = int(tokens[-1].replace('"', ''))
	
	r = get_code_redundancy(n, k)
	t = get_file_transfer_time(n, k, N_c, N)
	line = (p, n, k, r, t)
	print(*line, sep=separator)
	a.append(line)

print('table 3')
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
