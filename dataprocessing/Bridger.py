import pandas as pd
import numpy as np

# La classe Bridger si occupa di colmare i valori NaN all'interno del dataset
class Bridger:
    # Il metodo imputation va a colmare i valori nulli effettuando l'imputazione.
    # Prende in ingresso il dataset e restituisce il dataset modificato.
    def imputation(self, dataset):
        """
        Effettua l'imputazione dei valori nulli nel dataset.

        Parameters:
        dataset (DataFrame): Il DataFrame contenente il dataset.

        Returns:
        DataFrame: Il DataFrame modificato con i valori nulli colmati.
        """
        # Verifichiamo se ci sono valori nulli nel dataset
        if dataset.isnull().sum().any():
            # Se ci sono valori nulli, otteniamo le colonne con valori nulli
            col_Nan = dataset.columns[dataset.isnull().sum() > 0].tolist()

            # Per ogni colonna con valori nulli
            for col in col_Nan:
                # Se la colonna è 'Class', eliminiamo le righe con valori nulli
                if col == 'Class':
                    dataset = dataset[dataset[col].notna()]
                else:
                    # Altrimenti, calcoliamo la mediana dei valori e la sostituiamo
                    # al posto dei valori nulli nella colonna corrente
                    revenue_median = dataset[col].median()
                    dataset[col].fillna(revenue_median, inplace=True)

        return dataset
