import pandas as pd
from .Reader_dataset import Reader_dataset
from .Reader_dataset_csv import Reader_dataset_csv
from .Reader_dataset_json import Reader_dataset_json

#la classe Reader_dataset_factory instanzia la giusta classe in base all'estensione del file di input
class Reader_dataset_factory:

    # Il metodo "readerFactoryManager" accetta il percorso di un file come input e, in funzione dell'estensione del file,
    # nel caso in cui il formato non sia csv o json, gestisce l'eccezione avvertendo di inserire un file path con una
    # estensione supportata e dà la possibilità di inserire un nuovo filepath

    def readerFactoryManager(self, filepath):
        try:
            if filepath.endswith('.csv'):
                return Reader_dataset_csv().parse(filepath)
            elif filepath.endswith('.json'):
                return Reader_dataset_json().parse(filepath)
            else:
                raise RuntimeError("L'estensione del file non è tra quelle supportate .")
        except RuntimeError as error:
            print(error)
            print("\nCambia l'estensione del file in csv o json")
            print("Inserisci un nuovo filepath:")
            new_filepath = input()
            return self.readerFactoryManager(new_filepath)
