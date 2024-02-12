import pandas as pd
from .Reader_dataset import Reader_dataset
# Importiamo la classe astratta Reader_dataset
# La classe Reader_dataset_csv si occupa di leggere un dataset con estensione csv
class Reader_dataset_csv(Reader_dataset):
    # Il metodo parse prende in ingresso il percorso del file e restituisce in uscita un dataset
    def parse(self, filepath):
        # Leggiamo il file CSV  e lo salviamo in un DataFrame
        df_csv = pd.read_csv(filepath)

        # Poiché il 'Sample code number' non è univoco per ogni campione, lo indicizziamo in modo univoco
        # tramite una sequenza di numeri crescenti
        df_csv['Sample code number'] = range(1, len(df_csv) + 1)

        # Impostiamo l'indice del DataFrame sulla nuova colonna 'Sample code number'
        df_csv = df_csv.set_index('Sample code number')

        # Restituiamo il DataFrame con l'indice univoco
        return df_csv
