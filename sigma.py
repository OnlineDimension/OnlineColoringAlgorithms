from math import ceil

X=[(1,2),(1,2.2),(1,2.5)]
b=1
n=100
sigma=1.5

def CGJMP(X, n=100, b=2, sigma=1.5):
	# This is an implemenation of the algorithm for Theorem 3 of the 2024 paper by Chybowska-Sokol et al.
	
	phi = ceil(b*(1+sigma))
	S = [0]*n
	L = [0]*n
	out = []

	for I in X:
		# Check that interval has valid length
		if I[1]-I[0] > sigma:
			print("The interval", I, "is too long.")
			return
		if I[1]-I[0] < 1:
			print("The interval", I, "is too short.")
			return
		if I[0] < 0 or I[1]> (n/b)//1:
			print("The interval", I, "is out of bounds.")
			return
			
		#1. Let i be the index of the small block containing the left endpoint of the interval
		i = int((I[0]*b)//1)

		#2. Let j be the index of the large block containing the left endpoint of the interval such that j = S[i] mod b
		# Fancy version: j = (S[i]%b == i%b) + 1
		if S[i]%b == i%b:
			j = i
		else:
			j = i - 1

		#3. Assign the interval the color (j mod phi, L[j])
		out.append((j%phi,L[j]))

		#4. Increase the small counter by 1
		S[i] += 1

		#5. Increase the large counter by 1
		L[j] += 1

	return out

def chromatic(X):
	# Find the chromatic number of X to compute the competitive ratio.
	M = 0
	count = 0
	Endpoints = []

	for I in X:
		Endpoints.append((X[0],1))
		Endpoints.append((X[1],-1))
	Endpoints.sort()
	
	for e in Endpoints:
		count += e[1]
		M = max(M, count)

	return M

def CR(X, colors):
	# Compute the competitive ratio
	bag = set()
	count = 0
	for color in colors:
		if color not in bag:
			count += 1
			bag.add(color)
	return count/chromatic(X)

colors = CGJMP(X)
for i in range(len(X)):
	print(X[i], ":",  colors[i])
R = CR(X, colors)
print("The competitive ratio is", R)
