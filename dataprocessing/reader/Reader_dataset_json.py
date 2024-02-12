import pandas as pd
from .Reader_dataset import Reader_dataset  # Importa la classe astratta Reader_dataset


# La classe Reader_dataset_json si occupa di leggere un dataset con estensione JSON
class Reader_dataset_json(Reader_dataset):
    def parse(self, filepath):
        """
        Metodo per analizzare un file JSON e restituire un DataFrame.

        Parameters:
        filepath (str): Percorso del file JSON.

        Returns:
        pandas.DataFrame: DataFrame contenente i dati del file JSON.
        """
        # Legge il file JSON e lo converte in un DataFrame
        df_json = pd.read_json(filepath)

        # Essendo che il 'Sample code number' non è univoco per ogni campione, lo indicizza in ordine crescente ed univoco
        df_json['Sample code number'] = range(1, len(df_json) + 1)

        # Imposta la colonna 'Sample code number' come indice del DataFrame
        df_json = df_json.set_index('Sample code number')

        return df_json
