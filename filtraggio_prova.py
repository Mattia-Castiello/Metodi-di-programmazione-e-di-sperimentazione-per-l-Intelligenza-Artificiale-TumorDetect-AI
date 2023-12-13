import json
import pandas as pd

# Carica il tuo file CSV
df = pd.read_csv("dataset/breast_cancer.csv")

# Dividi il dataset per classe
benigno = df[df['Class'] == 2]
maligno = df[df['Class'] == 4]

# Seleziona il 75% del benigno e il 25% del maligno
percentuale_benigno = 0.75
percentuale_maligno = 0.25

# Calcola il numero di campioni da prelevare per ogni classe
n_campioni_benigno = min(int(percentuale_benigno * 150), len(benigno))
n_campioni_maligno = min(150 - n_campioni_benigno, len(maligno))

# Preleva casualmente il numero desiderato di campioni da ciascuna classe
sottoclasse_benigno = benigno.sample(n=n_campioni_benigno)
sottoclasse_maligno = maligno.sample(n=n_campioni_maligno)

# Concatena i due sottoinsiemi
sottodataset = pd.concat([sottoclasse_benigno, sottoclasse_maligno])

# Visualizza il risultato
print("Dimensioni del sottoinsieme:", sottodataset.shape)
print("Conteggio per classe:\n", sottodataset['Class'].value_counts())

# Ottieni l'input da terminale
input_string = input("Inserisci i dati nel formato: ")

# Suddividi la stringa in una lista di valori
input_values = input_string.split(',')

# Verifica che la lista abbia il numero corretto di valori
if len(input_values) == 9:
    # Crea il dizionario
    nuovo_dato = {
        'Clump Thickness': int(input_values[0]),
        'Uniformity of Cell Size': int(input_values[1]),
        'Uniformity of Cell Shape': int(input_values[2]),
        'Marginal Adhesion': int(input_values[3]),
        'Single Epithelial Cell Size': int(input_values[4]),
        'Bare Nuclei': int(input_values[5]),
        'Bland Chromatin': int(input_values[6]),
        'Normal Nucleoli': int(input_values[7]),
        'Mitoses': int(input_values[8])
    }

    # Visualizza il risultato
    print("\nNuovo dato inserito:")
    print(json.dumps(nuovo_dato, indent=4))  # indent=4 fornisce un formato indentato e più leggibile

    # Crea range di valori per ciascuna caratteristica e classe
    range_valori = {}

    for colonna in sottodataset.columns[:-1]:  # Ignora l'ultima colonna 'Class'
        if colonna != 'Sample code number':
            min_val_benigno = sottodataset[sottodataset['Class'] == 2][colonna].min()
            max_val_benigno = sottodataset[sottodataset['Class'] == 2][colonna].max()
            min_val_maligno = sottodataset[sottodataset['Class'] == 4][colonna].min()
            max_val_maligno = sottodataset[sottodataset['Class'] == 4][colonna].max()

            range_valori[colonna] = {
                'Benigno': (min_val_benigno, max_val_benigno),
                'Maligno': (min_val_maligno, max_val_maligno)
            }

    # Funzione per classificare un nuovo dato
    def classifica_nuovo_dato(nuovo_dato):
        conteggio_benigno = 0
        conteggio_maligno = 0

        for colonna, valori in range_valori.items():
            valore_nuovo_dato = nuovo_dato[colonna]

            for classe, range_classe in valori.items():
                if range_classe[0] <= valore_nuovo_dato <= range_classe[1]:
                    if classe == 'Benigno':
                        conteggio_benigno += 1
                    else:
                        conteggio_maligno += 1

        if conteggio_benigno > conteggio_maligno:
            return 'Benigno'
        else:
            return 'Maligno'

    # Classifica il nuovo dato
    risultato_classificazione = classifica_nuovo_dato(nuovo_dato)

    # Visualizza il risultato
    print("\nClassificazione del nuovo dato:")
    print(f"\t- Tumore: {risultato_classificazione}")

else:
    print("Errore: Assicurati di inserire 9 valori separati da virgole.")

# Casi di test:
# - Benigno: 4,1,1,1,2,1,2,1,1
# - Maligno: 10,7,7,6,4,10,4,1,2