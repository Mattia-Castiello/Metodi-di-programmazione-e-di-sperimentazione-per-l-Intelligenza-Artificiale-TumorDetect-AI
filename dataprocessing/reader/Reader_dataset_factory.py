import os
from .Reader_dataset_csv import Reader_dataset_csv
from .Reader_dataset_json import Reader_dataset_json

# La classe Reader_dataset_factory instanzia la giusta classe in base all'estensione del file di input
class Reader_dataset_factory:
    """
    Factory per la creazione di oggetti Reader_dataset_csv o Reader_dataset_json in base all'estensione del file.

    Attributes:
    None
    """

    def readerFactoryManager(self, filepath):
        """
        Gestisce la creazione dell'oggetto Reader_dataset appropriato in base all'estensione del file.

        Parameters:
        filepath (str): Il percorso del file.

        Returns:
        DataFrame: Il DataFrame contenente il dataset.
        """
        try:
            if os.path.isfile(filepath):  # Verifica se il file esiste nel percorso specificato
                if filepath.endswith('.csv'):
                    # Se l'estensione del file è .csv, istanzia Reader_dataset_csv e chiama il metodo parse
                    return Reader_dataset_csv().parse(filepath)
                elif filepath.endswith('.json'):
                    # Se l'estensione del file è .json, istanzia Reader_dataset_json e chiama il metodo parse
                    return Reader_dataset_json().parse(filepath)
                else:
                    # Se l'estensione del file non è tra quelle supportate, solleva un'eccezione
                    raise RuntimeError("L'estensione del file non è tra quelle supportate.")
        except RuntimeError as error:
                # Se viene sollevata un'eccezione, avvisa l'utente di cambiare l'estensione del file
                # e chiede di inserire un nuovo filepath
                print(error)
                print("Cambia l'estensione del file in csv o json")
                return None

