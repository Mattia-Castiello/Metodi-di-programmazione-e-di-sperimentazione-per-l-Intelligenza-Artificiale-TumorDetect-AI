from dataprocessing.reader.Reader_dataset_factory import Reader_dataset_factory

class Input:
    def __init__(self, path_dataset=None, k=None, evaluation=None, training=None, K=None, weight = 'uniform', metrics=[], data=None):
        self.k = k
        self.evaluation = evaluation
        self.training = training
        self.K = K
        self.weight = weight
        self.metrics = metrics
        self.path_dataset = path_dataset
        self.data = data

    def get_path(self):
        while True:
            self.path_dataset = input("Inserisci il percorso del dataset: ")
            if self.path_dataset.startswith('"') and self.path_dataset.endswith('"'):
                self.path_dataset = self.path_dataset[1:-1]  # Rimuove i doppi apici
            try:
                self.data = Reader_dataset_factory().readerFactoryManager(self.path_dataset)
                if self.data is not None:
                    break
                else:
                    print(f"Il file '{self.path_dataset}' non è stato trovato.")
            except FileNotFoundError:
                print(f"Il file '{self.path_dataset}' non è stato trovato.")

    def get_k(self):
        while True:
            try:
                self.k = int(input("Inserisci il numero di vicini da utilizzare per il classificatore: "))
                break
            except ValueError:
                print("Errore: Inserisci un numero intero valido.")

    def get_evaluation_method(self):
        print("Scegli come valutare il modello:")
        print("1. Holdout")
        print("2. KFold (KFoldCrossValidation)")
        while True:
            try:
                choice = int(input("Inserisci il numero corrispondente alla tua scelta: "))
                if choice == 1:
                    self.evaluation = 1
                    break
                elif choice == 2:
                    self.evaluation = 2
                    self.get_K()
                    break
                else:
                    print("Errore: Inserisci un numero valido.")
            except ValueError:
                print("Errore: Inserisci un numero intero valido.")

    def get_training_percentage(self):
        while True:
            try:
                self.training = int(input("Inserisci la percentuale di dati da utilizzare nel set di training (0-100): "))
                if 0 < self.training < 100:
                    break
                else:
                    print("Errore: Inserisci un numero intero valido compreso tra 0 e 100.")
            except ValueError:
                print("Errore: Inserisci un numero intero valido.")

    def get_weight_method(self):
        print("Scegli il metodo di pesatura da utilizzare per il calcolo del KNN:")
        print("1. Uniforme - se la misura della distanza è uniforme, prende la moda dei vicini più prossimi")
        print("2. Distanza - se la misura della distanza non è uniforme, prende la media ponderata dei vicini più prossimi")
        while True:
            try:
                choice = int(input("Inserisci il numero corrispondente alla tua scelta: "))
                if choice == 1:
                    self.weight = 'uniform'
                    break
                elif choice == 2:
                    self.weight = 'distance'
                    break
                else:
                    print("Errore: Inserisci un numero valido.")
            except ValueError:
                print("Errore: Inserisci un numero intero valido.")

    def get_K(self):
        while True:
            try:
                self.K = int(input("Inserisci il numero di esperimenti K: "))
                if self.K > 0:
                    break
                else:
                    print("Errore: Inserisci un numero intero valido maggiore di 0.")
            except ValueError:
                print("Errore: Inserisci un numero intero valido.")

    def choose_metrics(self):
        print("Scegli quali metriche devono essere validate:")
        print("1. Accuracy Rate")
        print("2. Error Rate")
        print("3. Sensitivity")
        print("4. Specificity")
        print("5. Geometric Mean")
        print("6. Tutte le metriche disponibili")
        while True:
            choices = input("Inserisci i numeri corrispondenti alle metriche separate da uno spazio: ")
            choices = choices.split()
            valid_choices = ["1", "2", "3", "4", "5", "6"]
            if all(choice in valid_choices for choice in choices):
                break
            else:
                print("Errore: Inserisci numeri validi.")

        for choice in choices:
            if choice == "1":
                self.metrics.append(1)
            elif choice == "2":
                self.metrics.append(2)
            elif choice == "3":
                self.metrics.append(3)
            elif choice == "4":
                self.metrics.append(4)
            elif choice == "5":
                self.metrics.append(5)
            elif choice == "6":
                self.metrics = [1, 2, 3, 4, 5]
                break

    def get_input(self):
        self.get_path()
        self.get_k()
        self.get_training_percentage()
        self.get_evaluation_method()
        self.get_weight_method()
        self.choose_metrics()
        return self
