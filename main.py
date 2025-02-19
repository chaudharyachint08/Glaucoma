import os

import numpy as np
from skimage.io import imread, imshow
from skimage.feature import hog
from skimage.transform import resize

import matplotlib.pyplot as plt

dataset = 'Database-1'
true_path, false_path = 'Glaucoma', 'Healthy'

orientations, pixels_per_cell, cells_per_block = 8, 64 , 1

MAX_H, MAX_W = 0, 0
for path in  true_path, false_path:
	ls = sorted(((img,imread(os.path.join('.',dataset,path,img)).shape) for img in os.listdir(os.path.join('.',dataset,path))),key=lambda x:x[1][0]*x[1][1], reverse=True)
	print( 'Total Shapes in {0} is {1:d}'.format(path,len(set(x[1] for x in ls))) )
	print(*set(x[1] for x in ls),sep='\n')
	MAX_H, MAX_W = max(MAX_H,max(x[1][0] for x in ls)), max(MAX_W,max(x[1][1] for x in ls))
MAX_H, MAX_W = int(pixels_per_cell*np.ceil(MAX_H/pixels_per_cell)), int(pixels_per_cell*np.ceil(MAX_W/pixels_per_cell))
print('Maximum Chosen Height is {0:d} pixels and width is {1:d} pixels'.format(MAX_H, MAX_W))




def hog_of_path(path, orientations=10, pixels_per_cell=16, cells_per_block=2):
	res = []
	for img_name in os.listdir(os.path.join('.',dataset,path)):
		img_mat = imread(os.path.join('.',dataset,path,img_name))
		img_mat = resize(img_mat,(MAX_H, MAX_W))
		hog_vec = hog(img_mat, orientations=orientations, pixels_per_cell=(pixels_per_cell,pixels_per_cell), cells_per_block=(cells_per_block,cells_per_block))
		res.append( hog_vec )
	return np.array(res)

def get_data(dataset):
	x,y = [], []
	for path, label in zip((true_path,false_path),(1,0)):
		hog_ls = hog_of_path(path, orientations=orientations, pixels_per_cell=pixels_per_cell, cells_per_block=cells_per_block)
		x.extend(hog_ls)
		y.extend([label]*len(hog_ls))
	return np.array(x), np.array(y)

x,y = get_data(dataset)



from sklearn.model_selection import StratifiedKFold

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble     import RandomForestClassifier
from sklearn.neighbors    import KNeighborsClassifier
  
from sklearn.metrics import accuracy_score

skf = StratifiedKFold(n_splits=5)


knn = KNeighborsClassifier(n_neighbors=5)

for trn, tst in skf.split(x,y):
	_ = knn.fit(x[trn],y[trn])
	print( knn.score(x[tst],y[tst]), accuracy_score(knn.predict(x[tst]),y[tst]) )

lg = LogisticRegression()
for trn, tst in skf.split(x,y):
	_ = lg.fit(x[trn],y[trn])
	print( lg.score(x[tst],y[tst]), accuracy_score(lg.predict(x[tst]),y[tst]) )

rf = RandomForestClassifier(max_features=40, max_depth=10)
for trn, tst in skf.split(x,y):
	_ = rf.fit(x[trn],y[trn])
	print( rf.score(x[tst],y[tst]), accuracy_score(rf.predict(x[tst]),y[tst]) )


