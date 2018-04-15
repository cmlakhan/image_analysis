import numpy as np
import csv as csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt








def reformat_images(image_corpus, x, y, c):
    ims = image_corpus.reshape(image_corpus.shape[0],c,x,y).transpose([0,2, 3, 1])
    return ims



def generate_figures(X,Y,labels,numFigures):
    numRows=X.shape[0]
    idx = np.random.randint(numRows, size=numFigures)
    imageSubset=X[idx,:]
    labelSubset=Y[idx]
    return imageSubset, [labels[labelSubset[i]] for i in range(numFigures)]




def show_images(images, cols=1, titles=None):
    """Display a list of images in a single figure with matplotlib.

    Parameters
    ---------
    images: List of np.arrays compatible with plt.imshow.

    cols (Default = 1): Number of columns in figure (number of rows is
                        set to np.ceil(n_images/float(cols))).

    titles: List of titles corresponding to each image. Must have
            the same length as titles.
    """
    assert ((titles is None) or (len(images) == len(titles)))
    n_images = len(images)
    if titles is None: titles = ['Image (%d)' % i for i in range(1, n_images + 1)]
    fig = plt.figure()
    for n, (image, title) in enumerate(zip(images, titles)):
        a = fig.add_subplot(cols, np.ceil(n_images / float(cols)), n + 1)
        if image.ndim == 2:
            plt.gray()
        plt.imshow(image)
        a.set_title(title)
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_images)
    plt.show()
