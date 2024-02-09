import pandas as pd
import numpy as np

#La classe bridger si occupa di colmare i valori Nan all'interno del dataset

class Bridger:
    # il metodo impution va a colmare i valori nulli effettuando l'imputazione
    # prende in ingresso il dataset e restituisce il dataset modificato
    def impution(self, dataset):
        if dataset.isnull().sum().any():
            col_Nan = dataset.columns[dataset.isnull().sum() > 0].tolist()
            # calcoliamo la mediana dei valori e la sostituiamo al posto dei valori nulli
            # scegliamo la mediana poichè inserisce valori interi
            #inoltre se il valore nullo appartiene alla colonna Class eliminiamo la riga
            #in modo da non assegnare un tumore a pazienti sani e viceversa

            for col in col_Nan:
                if col == 'Class':
                    dataset = dataset[dataset[col].notna()]
                else:
                    revenue_median = dataset[col].median()
                    dataset[col].fillna(revenue_median, inplace=True)
        return dataset
