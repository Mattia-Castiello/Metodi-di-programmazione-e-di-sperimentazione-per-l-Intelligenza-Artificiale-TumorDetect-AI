import pandas as pd
from .Reader_dataset import Reader_dataset
#importiamo la classe astratta

#la classe Reader_dataset_csv si occupa di leggere un dataset con estensione csv
class Reader_dataset_csv(Reader_dataset):
    #il metodo parse prende in ingresso il percorso del file e restituisce in uscita un dataset
    def parse(self, filepath):
        df_csv=pd.read_csv(filepath)

        #essendo che il sample code number non è univoco per ogni campione andiamo
        #ad indicizzare la colonna in ordine crescente ed univoca

        df_csv['Sample code number'] = range(1, len(df_csv) + 1)

        df_csv = df_csv.set_index('Sample code number')
        return df_csv