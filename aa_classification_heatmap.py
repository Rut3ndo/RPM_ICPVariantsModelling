import numpy as np; np.random.seed(0)
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns; sns.set()
from matplotlib.colors import LinearSegmentedColormap

aa_class_feature = pd.read_csv("aa_sub_classification_ABCB4_ABCB11.csv")
#print("HERE")
#flights = sns.load_dataset(r"C:\Users\charles.sharpe\OneDrive - Global Graphics PLC\Documents\1_CS\RMP_HeatMap\EDIT_flights.csv")
#flights = sns.load_da
feature_change = (aa_class_feature)
feature_change = feature_change.pivot("Feature","Var", "Change")
'''
#ax = sns.heatmap(data, xticklabels=2, yticklabels=False)
grid_kws = {"height_ratios": (.6, .05), "hspace": .2}
f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws)

ax = sns.heatmap(flights, ax=ax,
                 cbar_ax=cbar_ax,
                 cbar_kws={"orientation": "vertical"})
'''
#f, ax = plt.subplots(figsize=(9, 6))
#ax = sns.heatmap(flights)


##
myColors = ("seashell", "steelblue")
cmap = LinearSegmentedColormap.from_list('Custom', myColors, 2)
##

ax = sns.heatmap(feature_change, annot= False, linewidths=.5, cmap= cmap, square = True)

# Manually specify colorbar labelling after it's been generated
colorbar = ax.collections[0].colorbar
colorbar.set_ticks([0, 1])
colorbar.set_ticklabels(['No Change', 'Change'])

# X - Y axis labels
ax.set_ylabel('Feature')
ax.set_xlabel('ICP  variant')

# Only y-axis labels need their rotation set, x-axis labels already have a rotation of 0
_, labels = plt.yticks()
plt.setp(labels, rotation=0)

plt.show()
