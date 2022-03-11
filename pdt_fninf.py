#!/usr/bin/python
#-*- encoding:utf-8 -*-
import numpy as np

#loading data
T_dict = np.load('./knowledge_data/T_dict.npy',allow_pickle = True).item()
D_dict = np.load('./knowledge_data/D_dict.npy',allow_pickle = True).item()
P_dict = np.load('./knowledge_data/P_dict.npy',allow_pickle = True).item()
DB_retrieval_dict = np.load('./knowledge_data/DB_retrieval_dict.npy',allow_pickle = True).item()
T_retrieval_dict = np.load('./knowledge_data/T_retrieval_dict.npy',allow_pickle = True).item()

Mod_name = ["Clinical/Behavioral",	"Neuroimaging",	"Electrophysiology", "Molecular"]
Sorted_DB_cat_list = ['Healthy', 'Autism', 'ADHD', 'Schizophrenia', 'Bipolar disorder', 'Sleep', 'Epilepsy', 'Traumatic brain injury', 'Stroke', 'Cancer', 'AD', 'Other']
Pha_map_list = ["Data Capture", "Quality control", "Data Analysis", "Data Visualization", "Data Management","Data Sharing"]

def pdt_fninf(k_type, sel_condition):
    import json
    if k_type == "Project":
        #result = json.dumps(P_dict)
        result = P_dict
    if k_type == "Database":
        if len(sel_condition) == 0:
            result = D_dict
        else:
            Mod_condition = [var for var in sel_condition if var in Mod_name]
            DB_cat_condition = [var for var in sel_condition if var in Sorted_DB_cat_list]
            if len(Mod_condition) != 0 and len(DB_cat_condition) != 0:
                row_info, col_info = [], []
                for i in Mod_condition:
                    row_info.extend(DB_retrieval_dict[i]) 
                for j in DB_cat_condition:
                    col_info.extend(DB_retrieval_dict[j])
                query_keys = list(set(row_info).intersection(set(col_info)))
                query_dict = {}
                for k in query_keys:
                    if k not in query_dict.keys():
                        query_dict[k] = D_dict[k]
                    else:
                        continue
                result = query_dict
            elif len(Mod_condition) != 0:
                print('weclome hdliang to retrieval this knowledge base')
                col_info = []
                for i in Mod_condition:
                    col_info.extend(DB_retrieval_dict[i])
                query_keys = list(set(col_info))
                query_dict = {}
                for k in query_keys:
                    if k not in query_dict.keys():
                        query_dict[k] = D_dict[k]
                    else:
                        continue
                result = query_dict
            else:
                row_info = []
                for i in DB_cat_condition:
                    row_info.extend(DB_retrieval_dict[i])
                query_keys = list(set(row_info))
                query_dict = {}
                for k in query_keys:
                    if k not in query_dict.keys():
                        query_dict[k] = D_dict[k]
                    else:
                        continue
                #result = json.dumps(query_dict)
                result = query_dict
    if k_type == "Toolkit":
        if len(sel_condition) == 0:
            result = T_dict
        else:
            Mod_condition = [var for var in sel_condition if var in Mod_name]
            T_phase_condition = [var for var in sel_condition if var in Pha_map_list]
            if len(Mod_condition) != 0 and len(T_phase_condition) != 0:
                row_info, col_info = [], []
                for i in Mod_condition:
                    row_info.extend(T_retrieval_dict[i]) 
                for j in T_phase_condition:
                    col_info.extend(T_retrieval_dict[j])
                query_keys = list(set(row_info).intersection(set(col_info)))
                query_dict = {}
                for k in query_keys:
                    if k not in query_dict.keys():
                        query_dict[k] = T_dict[k]
                    else:
                        continue
                result = query_dict
            elif len(Mod_condition) != 0:
                col_info = []
                for i in Mod_condition:
                    col_info.extend(T_retrieval_dict[i])
                query_keys = list(set(col_info))
                query_dict = {}
                for k in query_keys:
                    if k not in query_dict.keys():
                        query_dict[k] = T_dict[k]
                    else:
                        continue
                result = query_dict
            else:
                row_info = []
                for i in T_phase_condition:
                    row_info.extend(T_retrieval_dict[i])
                query_keys = list(set(row_info))
                query_dict = {}
                for k in query_keys:
                    if k not in query_dict.keys():
                        query_dict[k] = T_dict[k]
                    else:
                        continue
                #result = json.dumps(query_dict)
                result = query_dict
    
    return json.dumps(result)
    #return list(result.keys())

if __name__=="__main__":

    Mod_name = ["Clinical/Behavioral",	"Neuroimaging",	"Electrophysiology", "Molecular"]
    Sorted_DB_cat_list = ['Healthy', 'Autism', 'ADHD', 'Schizophrenia', 'Bipolar disorder', 'Sleep', 'Epilepsy', 'Traumatic brain injury', 'Stroke', 'Cancer', 'AD', 'Other']
    Pha_map_list = ["Data Capture", "Quality control", "Data Analysis", "Data Visualization", "Data Management","Data Sharing"]
    
    k_type = 'Database'
    sel_condition = ['AD']
    result = pdt_fninf(k_type, sel_condition)
    print(result)

