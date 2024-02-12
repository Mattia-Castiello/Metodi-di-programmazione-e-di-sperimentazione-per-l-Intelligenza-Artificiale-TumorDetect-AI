import pandas as pd
from .Reader_dataset import Reader_dataset
from .Reader_dataset_csv import Reader_dataset_csv
from .Reader_dataset_json import Reader_dataset_json

#la classe Reader_dataset_factory instanzia la giusta classe in base all'estensione del file di input
class Reader_dataset_factory:

    # Il metodo "readerFactoryManager" accetta il percorso di un file come input e, in funzione dell'estensione del file,
    # istanzia il corretto oggetto "dataprocessing".
    # nel caso in cui il formato non sia csv o json, gestisce l'eccezione convertendo il filename in un file csv,
    # inoltre istanzia il lettore di un file csv
    def readerFactoryManager(self, filepath):
        try:
            if filepath.endswith('.csv'):
                return Reader_dataset_csv().parse(filepath)
            elif filepath.endswith('.json'):
                return Reader_dataset_json().parse(filepath)
        except RuntimeError:
                print("Unrecognized file format for the dataset")
                print("\nChange the file extension to CSV")
                # Non ha senso convertire il percorso in un file CSV, quindi potresti gestire diversamente questa eccezione
