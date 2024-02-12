import pandas as pd
import numpy as np

# La classe Bridger si occupa di colmare i valori NaN all'interno del dataset
class Bridger:
    # Il metodo impution va a colmare i valori nulli effettuando l'imputazione.
    # Prende in ingresso il dataset e restituisce il dataset modificato.
    def impution(self, dataset):
        """
        Effettua l'imputazione dei valori nulli nel dataset.

        Parameters:
        dataset (DataFrame): Il DataFrame contenente il dataset.

        Returns:
        DataFrame: Il DataFrame modificato con i valori nulli colmati.
        """
        # Facciamo una copia del DataFrame originale per evitare modifiche inplace
        dataset_copy = dataset.copy()

        # Verifichiamo se ci sono valori nulli nel dataset
        if dataset_copy.isnull().sum().any():
            # Se ci sono valori nulli, otteniamo le colonne con valori nulli
            col_Nan = dataset_copy.columns[dataset_copy.isnull().sum() > 0].tolist()

            # Per ogni colonna con valori nulli
            for col in col_Nan:
                # Se la colonna è 'Class', eliminiamo le righe con valori nulli
                if col == 'Class':
                    dataset_copy = dataset_copy.dropna(subset=[col])
                else:
                    # Altrimenti, calcoliamo la mediana dei valori e la sostituiamo
                    # al posto dei valori nulli nella colonna corrente
                    revenue_median = dataset_copy[col].median()
                    dataset_copy[col].fillna(revenue_median, inplace=True)

        return dataset_copy
