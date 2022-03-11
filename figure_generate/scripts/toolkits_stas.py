#!/usr/bin/python
#-*- encoding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# loading data
Toolkit_matrix = np.load('./figure_data/Toolkits_Modality_Data-life-cycle.npy')
Pha_name_list = ["Data Capture", "Quality control", "Data Analysis", "Data Visualization", "Data Management","Data Sharing"]
Mod_name = ["Clinical/Behavioral",	"Neuroimaging",	"Electrophysiology", "Molecular"]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

Toolkit_matrix = np.ma.log(Toolkit_matrix).filled(0)
sns.set(font_scale= 1.0)
#sns.heatmap(data=DB_toolkit_matrix, annot=True, fmt="f", linewidths= 0.3, linecolor= "grey", cmap= "RdBu_r")
fig, ax1 = plt.subplots()
ax1 = sns.heatmap(data=Toolkit_matrix, ax =ax1, annot=True, fmt="f", linewidths= 0.3, linecolor= "grey", cmap= "RdBu_r", xticklabels=Mod_name, yticklabels=Pha_name_list)

ax1.set_xlabel("Multi-modal data", size=16, weight='bold')
ax1.set_ylabel("Data life cycle",size=16, weight='bold')
ax1.set_title("Toolkits", size=18, weight='bold')
plt.xticks(rotation=0)
plt.show()
plt.close()