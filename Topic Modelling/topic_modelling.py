import numpy as np
import pandas as pd
import re, nltk, spacy, gensim

# Sklearn
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

# Plotting tools
import pyLDAvis
import pyLDAvis.sklearn
import matplotlib.pyplot as plt
import umap.umap_ as umap
import seaborn as sns

# Import Dataset
df = pd.read_csv('20-newsgroup-dataset.csv') # CHANGE THIS 
df = df.sample(frac=0.2, replace=False, random_state=1)
df.head()