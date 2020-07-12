import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns

def MinMaxScaler(X, min_val, max_val):
	X = (X-X.min())/((X.max()-X.min()))
	X = min_val + X*(max_val-min_val)
	return X

def StdScaler(X, mean=0, sigma=1):
	X = (X-X.mean())/X.std()
	X = mean+sigma*X
	return X

eps = None

def StandardData(N):
	global eps
	A   = abs(np.random.randn(N))
	if True or eps is None:
		eps = 1e-2*A.min()/A.max()
	A = MinMaxScaler(A,0,1)
	B = np.log(A+eps)
	B = MinMaxScaler(B,0,1)
	C = MinMaxScaler(StdScaler((A+B)/2,    0.5, 1),0,1)
	D = MinMaxScaler(StdScaler((A*B)**0.5, 0.5, 1),0,1)
	# E = MinMaxScaler(StdScaler((2*A*B)/(A+B+eps), 0.5, 1),0,1)

	sns.distplot(A, label='Original Tail Heavy Data')
	sns.distplot(B, label='Logarithmic Function of Data')
	sns.distplot(C, label='Arithmetic Mean of Combination')
	sns.distplot(D, label='Geometric Mean of Combination')
	# sns.distplot(E, label='Harmonic Mean of Combination')
	plt.grid(True)
	plt.legend()
	plt.xlabel('Scaled Data Range')
	plt.title('Handling Skewed Data')
	return A,B,C,D#,E

