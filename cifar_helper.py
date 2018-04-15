import numpy as np
import csv as csv
import numpy as np
import pandas as pd


labels = {0:'airplane',
          1:'automobile',
          2:'bird',
          3:'cat',
          4:'deer',
          5:'dog',
          6:'frog',
          7:'horse',
          8:'ship',
          9:'truck'
         }

def reformat_images(image_corpus, x, y, c):
    ims = image_corpus.reshape(image_corpus.shape[0],c,x, y).transpose([0,2, 3, 1])
    return ims




