import pandas as pd

# La classe DropDuplicate elimina i campioni duplicati presenti nel dataset
class DropDuplicate:
    """
    Classe per eliminare i campioni duplicati presenti nel dataset.

    Attributes:
    None
    """

    def drop(self, dataset):
        """
        Rimuove i campioni duplicati dal dataset.

        Parameters:
        dataset (DataFrame): Il DataFrame contenente il dataset.

        Returns:
        DataFrame: Il DataFrame senza campioni duplicati.
        """
        if dataset.duplicated().any():
            # Se ci sono campioni duplicati nel dataset, li elimina
            dataset = dataset.drop_duplicates()
        return dataset
