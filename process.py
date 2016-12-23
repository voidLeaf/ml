import numpy as np
import pandas as pd
import seaborn as sb
from nltk import FreqDist
biology = pd.read_csv("./input/biology.csv")
tags = []
for tag in biology["tags"]:
    for t in tag.split():
        tags.append(t)
fdist1 = FreqDist(tags)
print fdist1
fdist1.plot(50,cumulative=True)
