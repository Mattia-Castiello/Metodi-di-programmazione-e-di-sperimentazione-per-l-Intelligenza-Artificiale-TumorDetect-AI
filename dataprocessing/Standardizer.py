import pandas as pd
import numpy as np
class Standardizer:
    #il metodo standardizer effettua la standardizzazione dei valori che rientrano nelle features
    #mentre la colonna class  è identificata come target label
    #riceve in ingresso un dataset e restituisce il dataset diviso
    def standardization(self,dataset):
        for col in dataset.columns:
            if np.issubdtype(dataset[col].dtype,np.number) and col != 'Class':
                #calcolo della deviazione standard per ogni colonna
                std = dataset[col].std()
                #calcolo della media per ogni colonna
                mean = dataset[col].mean()
                #standardizzazione delle colonne che non sono class
                dataset[col] = (dataset[col] - mean) / std


        return dataset


    #il metodo split divide il dataset in due datset contenenti rispettivamente le figures in data e le labels in target
    def split(self, dataset):

        data = dataset.iloc[:, :-1]


        target = dataset.iloc[:, -1:]

        return data, target
