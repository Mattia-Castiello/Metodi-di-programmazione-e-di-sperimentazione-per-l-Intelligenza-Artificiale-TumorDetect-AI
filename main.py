class Input:
    def __init__(self):
        self.k = None
        self.validation_method = None
        self.training_percentage = None
        self.test_percentage = None
        self.num_experiments = None
        self.metrics = []

    def get_input(self):
        while True:
            try:
                self.k = int(input("Inserisci il numero di vicini da utilizzare per il classificatore: "))
                break
            except ValueError:
                print("Errore: Inserisci un numero intero valido.")

        print("Scegli come valutare il modello:")
        print("1. Holdout")
        print("2. KFold (KFoldCrossValidation)")
        while True:
            try:
                choice = int(input("Inserisci il numero corrispondente alla tua scelta: "))
                if choice == 1:
                    self.validation_method = "Holdout"
                    while True:
                        try:
                            self.training_percentage = float(input("Inserisci la percentuale di dati da utilizzare nel set di training: "))
                            break
                        except ValueError:
                            print("Errore: Inserisci un numero decimale valido.")
                    while True:
                        try:
                            self.test_percentage = float(input("Inserisci la percentuale di dati da utilizzare nel set di test: "))
                            break
                        except ValueError:
                            print("Errore: Inserisci un numero decimale valido.")
                    break
                elif choice == 2:
                    self.validation_method = "KFold"
                    while True:
                        try:
                            self.num_experiments = int(input("Inserisci il numero di esperimenti: "))
                            break
                        except ValueError:
                            print("Errore: Inserisci un numero intero valido.")
                    break
                else:
                    print("Errore: Inserisci un numero valido.")
            except ValueError:
                print("Errore: Inserisci un numero intero valido.")

        print("Scegli quali metriche devono essere validate:")
        print("1. Accuracy Rate")
        print("2. Error Rate")
        print("3. Sensitivity")
        print("4. Specificity")
        print("5. Geometric Mean")
        print("6. All the above")
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
                self.metrics.append("Accuracy Rate")
            elif choice == "2":
                self.metrics.append("Error Rate")
            elif choice == "3":
                self.metrics.append("Sensitivity")
            elif choice == "4":
                self.metrics.append("Specificity")
            elif choice == "5":
                self.metrics.append("Geometric Mean")
            elif choice == "6":
                self.metrics = ["Accuracy Rate", "Error Rate", "Sensitivity", "Specificity", "Geometric Mean"]
                break

def main():
    input_obj = Input()
    input_obj.get_input()
    # Add your code here to perform the desired operations based on the user input

if __name__ == "__main__":
    main()