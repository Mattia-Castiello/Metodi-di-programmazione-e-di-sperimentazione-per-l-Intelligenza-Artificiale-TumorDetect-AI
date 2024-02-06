import pandas as pd
import numpy as np
class Standardizer:
    #il metodo standardizer effettua la standardizzazione dei valori che rientrano nelle features
    #mentre la colonna class  è identificata come target label
    #riceve in ingresso un dataset e restituisce il dataset diviso
    def standardization(self,dataset):
        for col in dataset.columns:
            if np.issubdtype(dataset[col].dtype,np.number) and col != 'Class' and col!= 'Sample code number':
                #calcolo della deviazione standard per ogni colonna
                std = dataset[col].std()
                #calcolo della media per ogni colonna
                mean = dataset[col].mean()
                #standardizzazione delle colonne che non sono class e sample code number
                dataset[col] = (dataset[col] - mean) / std
                print(dataset)

        return dataset