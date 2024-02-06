from Reader_dataset_csv import Reader_dataset_csv
from Reader_dataset_json import Reader_dataset_json

#la classe Reader_dataset_factory instanzia la giusta classe in base all'estensione del file di input
class Reader_dataset_factory:

    # Il metodo "readerFactoryManager" accetta il nome di un file come input e, in funzione dell'estensione del file,
    # istanzia il corretto oggetto "reader".
    # nel caso in cui il formato non sia csv o json, gestisce l'eccezzione convertendo il filename in un file csv,
    # inoltre istanzianzia il lettore di un file csv
    def readerFactoryManager(self, filename):
        try:
            if filename.endswith('csv'):
                return Reader_dataset_csv()
            elif filename.endswith('json'):
                return Reader_dataset_json()
        except RuntimeError:
                print("Unrecognized file format for the dataset")
                print("\nChange the file extension to CSV")
                filename.to_csv('new_df.csv')
                return Reader_dataset_csv()
