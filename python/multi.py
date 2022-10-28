from functools import lru_cache
# def inc(ps, i, j):
# 	ps_ = ps[:]
# 	ps_[i] = (ps[i][0] + j, ps[i][1] + 1)
# 	return ps_

# def add(a, b):
# 	return (a[0] * b[1] + b[0] * a[1], a[1] * b[1])

# def inc(a):
# 	return (a[0] + a[1], a[1])

# def inv(a):
# 	return (-a[0], a[1])

# def prod(a, b):
# 	return (a[0] * b[0], a[1] * b[1])

# def E(n,ps):
# 	if n > 0:
# 		index, Q = -1, (0, 1)
# 		for i, p in enumerate(ps):
# 			E0 = E(n-1,inc(ps, i, 0))[1]
# 			E1 = E(n-1,inc(ps, i, 0))[1]
# 			q = add(prod(p, add(inc(E1), inv(E0))), E0)
# 			if q[0] * Q[1] > Q[0] * q[1]:
# 				index, Q = i, q
# 		return index, Q
# 	else:
# 		return (0, (0, 0))

def inc(ps, i, j):
	ps_ = ps[:]
	ps_[i] = (ps[i][0] + j, ps[i][1] + 1)
	return ps_

def prob(p):
	return p[0] / p[1]

def E(n,ps):
	if n > 0:
		index, Q = -1, 0
		for i, p in enumerate(ps):
			E0 = E(n - 1, inc(ps, i, 0))[1]
			E1 = E(n - 1, inc(ps, i, 1))[1]
			q = prob(p) * (1 + E1 - E0) + E0
			if q > Q:
				index, Q = i, q
		return index, Q
	else:
		return (0, 0)

Einf_dict = {}
def Einf(L, ps, n):
	key = (L, tuple(ps), n)
	if key not in Einf_dict:
		if n > 0:
			index, Q = -1, 0
			for i, p in enumerate(ps):
				E0 = Einf(L, inc(ps, i, 0), n - 1)[1]
				E1 = Einf(L, inc(ps, i, 1), n - 1)[1]
				q = prob(p) * (1 + E1 - E0) + E0
				if q > Q:
					index, Q = i, q
			Einf_dict[key] = index, L * Q
		else:
			Einf_dict[key] = (0, 0)
	return Einf_dict[key]

def find_limit(n, p0, m):
	lower = -m
	test = 0
	upper = m
	while upper > test and test > lower:
		if E(n, [p0, (test, m)])[0] == 1:
			upper = test
		else:
			lower = test
		test = (lower + upper) / 2
	return test

