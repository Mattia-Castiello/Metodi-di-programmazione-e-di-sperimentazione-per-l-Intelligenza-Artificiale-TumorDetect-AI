import pandas as pd
from .Reader_dataset import Reader_dataset
#importiamo la classe astratta

#la classe Reader_dataset_csv si occupa di leggere un dataset con estensione json
#la classe Reader_dataset_json si occupa di leggere un dataset con estensione json
class Reader_dataset_json(Reader_dataset):
    def parse(self, filepath):
        # il metodo parse prende in ingresso il percorso del file e restituisce in uscita un dataset

        df_json=pd.read_json(filepath)
        # essendo che il sample code number non è univoco per ogni campione andiamo
        # ad indicizzare la colonna in ordine crescente ed univoca

        df_json['Sample code number'] = range(1, len(df_json) + 1)

        df_json = df_json.set_index('Sample code number')

        return df_json