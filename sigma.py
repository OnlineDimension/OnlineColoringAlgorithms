from math import ceil

X=[(1,2),(1,2.2),(1,2.5)]
b=1
n=100
sigma=1.5

def f(X,b,n,sigma):

	phi=ceil(b*(1+sigma))
	S = [0]*n
	L = [0]*n
	out = []

	for I in X:
		#1. Let i be the index of the small block containing the left endpoint of the interval
		i = (I[0]*b)//1

		#2. Let j be the index of the large block containing the left endpoint of the interval such that j = S[i] mod b
		if S[i]%b == ((I[0]*b)//1)%b:
			j = (I[0]*b)//1
		else:
			j = ((I[0]*b)//1)+1

		#3. Assign the interval the color (j mod phi, L[j])
		out.append((j%phi,L[j]))

		#4. Increase the small counter by 1
		S[i] += 1

		#5. Increase the large counter by 1

		L[j] += 1

	return out

print(f(X,b,n,sigma))