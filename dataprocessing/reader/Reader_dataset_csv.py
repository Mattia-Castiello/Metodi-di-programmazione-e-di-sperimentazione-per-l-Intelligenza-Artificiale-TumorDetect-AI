import pandas as pd
from .Reader_dataset import Reader_dataset
# Importa la classe astratta Reader_dataset

# La classe Reader_dataset_csv si occupa di leggere un dataset con estensione CSV
class Reader_dataset_csv(Reader_dataset):
    def parse(self, filepath):
        """
        Metodo per analizzare un file CSV e restituire un DataFrame.

        Parameters:
        filepath (str): Percorso del file CSV.

        Returns:
        pandas.DataFrame: DataFrame contenente i dati del file CSV.
        """
        # Legge il file CSV e lo converte in un DataFrame
        df_csv = pd.read_csv(filepath)

        # Poiché il 'Sample code number' non è univoco per ogni campione, lo indicizza in ordine crescente ed univoco
        df_csv['Sample code number'] = range(1, len(df_csv) + 1)

        # Imposta la colonna 'Sample code number' come indice del DataFrame
        df_csv = df_csv.set_index('Sample code number')

        # Restituisce il DataFrame con l'indice univoco
        return df_csv
