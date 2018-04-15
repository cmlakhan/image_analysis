import numpy as np
import csv as csv
import numpy as np
import pandas as pd




def generate_figures(X,Y,labels,numFigures):
    numRows=X.shape[0]
    idx = np.random.randint(numRows, size=numFigures)
    print(idx)
    imageSubset=X[idx, :]
    labelSubset=Y[idx]
    return imageSubset, [labels[labelSubset[i]] for i in range(numFigures)]





