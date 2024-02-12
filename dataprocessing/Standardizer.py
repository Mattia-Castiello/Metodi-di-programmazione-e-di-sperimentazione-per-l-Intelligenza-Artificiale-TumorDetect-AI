import pandas as pd
import numpy as np

class Standardizer:
    """
    Classe per la standardizzazione dei valori delle features nel dataset.

    Attributes:
    None
    """

    def standardization(self, dataset):
        """
        Standardizza le features del dataset.

        Parameters:
        dataset (DataFrame): Il DataFrame contenente il dataset.

        Returns:
        DataFrame, DataFrame: Il DataFrame con le features standardizzate e la target label.
        """
        for col in dataset.columns:
            if np.issubdtype(dataset[col].dtype, np.number) and col != 'Class':
                # Calcolo della deviazione standard per la colonna
                std = dataset[col].std()
                # Calcolo della media per la colonna
                mean = dataset[col].mean()
                # Standardizzazione delle colonne che non sono 'Class'
                dataset[col] = (dataset[col] - mean) / std

        # Divisione del dataset in features (data) e target label (target)
        data, target = self.split(dataset)

        return data, target

    def split(self, dataset):
        """
        Divide il dataset in features e target label.

        Parameters:
        dataset (DataFrame): Il DataFrame contenente il dataset.

        Returns:
        DataFrame, DataFrame: Il DataFrame con le features e il DataFrame con la target label.
        """
        # Seleziona tutte le colonne tranne l'ultima ('Class') come features
        data = dataset.iloc[:, :-1]
        # Seleziona solo la colonna 'Class' come target label
        target = dataset.iloc[:, -1:]

        return data, target
