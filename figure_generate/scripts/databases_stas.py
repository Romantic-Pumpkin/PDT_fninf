#!/usr/bin/python
#-*- encoding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#loading data
DB_matrix = np.load('./figure_data/DB_Modality_Group.npy')
Sorted_DB_cat_list = ['Healthy', 'Autism', 'ADHD', 'Schizophrenia', 'Bipolar disorder', 'Sleep', 'Epilepsy', 'Traumatic brain injury', 'Stroke', 'Cancer', 'AD', 'Other']
Mod_name = ["Clinical/Behavioral",	"Neuroimaging",	"Electrophysiology", "Molecular"]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

DB_matrix = np.ma.log(DB_matrix).filled(0)
sns.set(font_scale= 1.0)
fig, ax1 = plt.subplots()
ax1 = sns.heatmap(data=DB_matrix, ax =ax1, annot=True, fmt="f", linewidths= 0.3, linecolor= "grey", cmap= "RdBu_r", xticklabels=Mod_name, yticklabels=Sorted_DB_cat_list)

ax1.set_xlabel("Multi-modal data", size=16, weight='bold')
ax1.set_ylabel("Different research groups", size=16, weight='bold')
ax1.set_title("Databases", size=18, weight='bold')

plt.xticks(rotation=0)
plt.show()
plt.close()
