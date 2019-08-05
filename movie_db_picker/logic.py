
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

train = pd.read_csv(r'train2.csv')
test = pd.read_csv(r'test2.csv')
lang ={
    'ja': 0,  'en': 1,  'fr': 2,  'de': 3,  'he': 4,
    'hi': 5,  'ru': 6,  'ka': 7,  'zh': 8,  'th': 9,
    'it': 10, 'es': 11, 'bn': 12, 'sv': 13, 'ko': 14,
    'sr': 15, 'da': 16, 'ta': 17, 'cs': 18, 'cn': 19,
    'ro': 20, 'ca': 21, 'no': 22, 'nl': 23, 'te': 24,
    'tr': 25, 'bm': 26, 'ml': 27, 'pt': 28, 'af': 29, 
    'fi': 30, 'ur': 31, 'el': 32, 'id': 33, 'xx': 34, 
    'pl': 35, 'kn': 36, 'is': 37, 'hu': 38, 'fa': 39, 
    'mr': 40, 'ar': 41, 'nb': 42, 'vi': 43          
        
    }
        
        
train.replace(lang, inplace=True)
test.replace(lang, inplace=True)
print(train.describe())


train.plot.scatter(x='original_language', y='revenue', s=50)
plt.savefig("filname.png")


