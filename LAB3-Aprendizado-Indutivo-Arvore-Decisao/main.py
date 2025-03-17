import pandas as pd
import numpy as np
from sklearn import tree, metrics
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from scipy.io import arff

data, meta = arff.loadarff('database.arff')

# Converter para DataFrame
df = pd.DataFrame(data)

# Encode da variável alvo ('class')
df['class'] = df['class'].map({b'tested_negative': 0, b'tested_positive': 1})

# Preencher valores ausentes com a moda
df.fillna(df.mode().iloc[0], inplace=True)

features = df.drop(columns=['class'])  # Matriz de features (X)
target = df['class']  # Variável alvo (y)

Arvore = DecisionTreeClassifier(criterion='entropy').fit(features, target)

plt.figure(figsize=(25, 10))
tree.plot_tree(Arvore, feature_names=features.columns,
               class_names=['tested_negative', 'tested_positive'],
               filled=True, rounded=True)

plt.savefig("decision_tree.png", dpi=1000, bbox_inches='tight')
plt.close()

fig, ax = plt.subplots(figsize=(10, 6))
metrics.ConfusionMatrixDisplay.from_estimator(Arvore, features, target,
                                              display_labels=['tested_negative', 'tested_positive'],
                                              values_format='d', ax=ax)

plt.savefig("confusion_matrix.png", dpi=300, bbox_inches='tight')
plt.close()