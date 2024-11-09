# from example import X, Y, Z
# import numpy as np

h = """size 12{ matrix {
2 {} # 1 {} # 3 {} # 2 {} # 1 {} #  {} # 5 {} # 4 {} ##
3 {} # 2 {} # 3 {} # 2 {} # 3 {} #  {} # 3 {} #  {} ##
2 {} # 1 {} # 2 {} # 1 {} # 2 {} # 3 {} # 4 {} # 4 {} ##
1 {} #  - 1 {} # 2 {} # 1 {} #  - 1 {} #  {} # 5 {} #  {} ##
1 {} #  - 1 {} # 2 {} #  - 2 {} # 2 {} # 3 {} # 6 {} # 5 {} ##
 {} # 1 {} # 3 {} # 1 {} #  {} #  {} # 7 {} #  {} ##
2 {} # 2 {} # 2 {} # 3 {} # 4 {} # 4 {} # 5 {} # 8 {} ##
3 {} # 4 {} # 2 {} # 4 {} # 2 {} # 5 {} # 6 {} # 5{}
} } {}"""
x = """size 12{ matrix {
4 {} # 1 {} # 3 {} #  {} # 3 {} # 7 {} #  {} # 6 {} ##
3 {} # 2 {} # 3 {} # 1 {} #  {} # 6 {} #  {} # 7 {} ##
4 {} # 2 {} # 3 {} # 3 {} # 2 {} # 5 {} # 5 {} # 6 {} ##
3 {} # 4 {} # 3 {} #  {} # 3 {} # 3 {} #  {} # 6 {} ##
 {} # 3 {} # 4 {} # 3 {} #  {} # 4 {} # 4 {} # 5 {} ##
2 {} # 3 {} # 2 {} # 1 {} # 3 {} # 2 {} # 2 {} # 4 {} ##
1 {} # 2 {} # 4 {} # 2 {} #  {} #  {} # 3 {} #  {} ##
4 {} # 5 {} #  {} # 5 {} # alignl { stack {
3 {} # 
 {} 
} }  {} # 4 {} #  {} # 5{}
} } {}"""

def get_number(s):
	if len(s) > 0:
		try:
			return int(s)
		except Exception:
			return 0
	return 0

def parse(text):
	res = []
	text = text.replace("{}", "")
	lines = text.split('\n')
	for line in lines:
		labels = line.split('#')
		labels = list(filter(lambda s: len(s) > 0, labels))
		cropped = list(map(lambda s: s.replace(" ", ""), labels))
		numeric = list(map(get_number, cropped))
		res.append(numeric)
	return res

if __name__ == "__main__":
	print(parse(h))
	print(parse(x))
