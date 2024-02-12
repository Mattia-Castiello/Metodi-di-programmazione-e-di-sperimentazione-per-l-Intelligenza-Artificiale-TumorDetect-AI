# Progetto_Progammazione_23-24
Questo progetto fa utilizzo di tecniche di machine learning per individuari tumori maligni e benigni. Per il nostro algoritmo abbiamo utlizzato il dataset Breast Cancer Wisconsin (Original). Per la fase di modelling è possibile scegliere  tra  il K-fold	Cross Validation e l'Holdout per una valutazione accurata. L'elemento centrale di questo studio è l'utilizzo del classificatore k-NN (k-Nearest Neighbors) per la categorizzazione dei tumori.

Il programma è progettato per offrire agli utenti diverse opzioni di input, consentendo una personalizzazione dettagliata dell'esecuzione e dell'analisi. Questa flessibilità si riflette nella presentazione dei risultati, che possono essere esplorati attraverso due modalità principali:

1. **Generazione di file di output dettagliati**: Questi file forniscono informazioni approfondite sulle prestazioni del modello e sui dati di input utilizzati.
2. **Visualizzazione di grafici esplicativi**: Questi grafici aiutano gli utenti a interpretare efficacemente le prestazioni del modello, fornendo preziose intuizioni nel campo della diagnostica dei tumori.

# Il Dataset breast_cancer.csv
Il dataset breast_cancer.csv è così formato:

- **Numero di Campioni**: 683 campioni.

- **Numero di Caratteristiche**: 11 caratteristiche per campione.

**Nomi delle Caratteristiche**:

- **Sample code number**: Identificativo unico per ogni campione.

- **Clump Thickness**: Spessore del grumo di cellule.

- **Uniformity of Cell Size**: Uniformità delle dimensioni cellulari.

- **Uniformity of Cell Shape**: Uniformità delle forme cellulari.

- **Marginal Adhesion**: Adesione marginale delle cellule.

- **Single Epithelial Cell Size**: Dimensione della singola cellula epiteliale.

- **Bare Nuclei**: Nuclei scoperti.

- **Bland Chromatin**: Cromatina blanda.

- **Normal Nucleoli**: Nucleoli normali.

- **Mitoses**: Tasso di mitosi.

- **Class**: Classificazione del tumore (2 per benigno, 4 per maligno).
 
è possibile trovare il dataset [qui](https://raw.githubusercontent.com/Mattia-Castiello/Progetto_Progammazione_23-24/main/breast_cancer.csv).

# Esecuzione  del Codice
Per mettere in funzione il codice di questo progetto, segui queste indicazioni:

- **Installazione dei Requisiti**: Prima di avviare l'applicazione, è indispensabile installare i requisiti. Questo può essere realizzato eseguendo il comando pip install -r requirements.txt nella cartella principale del progetto. Questo comando installerà tutte le librerie richieste, come numpy, pandas, matplotlib, ecc.

- **Importazione del Dataset**: Il dataset breast_cancer.csv è già presente nel repository e pronto per l'uso. Non c'è bisogno di scaricare o preparare ulteriormente il dataset.

- **Impostazione delle Opzioni di Input**: L'applicazione offre diverse opzioni di input per personalizzare l'esecuzione e l'analisi:

- **File di input**: Puoi indicare il percorso di un file CSV di input che contiene il dataset. Nel caso in cui l'estensione del file non sia .csv o .json, l'applicazione convertirà automaticamente il file in formato .csv

- **Numero di vicini (k) da utilizzare nel classificatore k-NN**: Questo parametro influisce su come il modello classifica i nuovi dati basandosi sui dati di addestramento.

# Metriche di valutazione
Queste scelte determinano il modo in cui vengono valutate le performance del modello. Le seguenti metriche sono disponibili:

- **Accuracy Rate**: Indica quante volte il nostro modello ha correttamente classificato correttamente un item nel nel nostro dataset rispetto al totale
- **Error Rate(TPR)**: Indica quante volte il nostro modello ha erroneamente classificato correttamente un item nel nel nostro dataset rispetto al totale
- **Sensitivity**: Indica la capacità del modello di individuare i casi positivi correttamente.
- **Specificity(TNR)**: Indica la capacità del modello di individuare i casi negativi corretamente.
- **Geometric Mean**: Misura l'equilibrio tra Sensibilità e Specificità.

Esecuzione del programma: Il programma può essere eseguito tramite il file "main.py", specificando le opzioni di input come argomenti della linea di comando, quando e come richiesto.

# Risultati
I risultati dell'esecuzione del programma sono presentati in due modi:
1) Se si sceglie come metodo di valutazione Holdout si otterrà un file di output "Metrics.txt" nel quale sono salvate le metriche di validazione del modello.
2) Se si sceglie come metodo di valutazione K-fold Cross Validation si otterrà un file di output "Metrics.txt", dove sono salvate le metriche di validazione del modello, e due plot:
  - 2.1) Boxplot: per ciascuna metrica mostra la distribuzione dei valori in tutti gli esperimenti.
  - 2.2) Line Plot: illustra per ciascuna metrica come i valori cambiano attraverso diversi esperimenti.

# Conclusioni
Questo progetto offre un'analisi delle prestazioni del classificatore k-NN nel contesto della diagnostica dei tumori. L'interfaccia utente è stata progettata per essere intuitiva e facile da usare, consentendo agli utenti di personalizzare l'esecuzione e l'analisi in base alle proprie esigenze. I risultati dell'analisi forniscono intuizioni sulle prestazioni del modello e sulle caratteristiche dei dati di input. Questo progetto può essere adattato per affrontare problemi di classificazione in altri contesti, consentendo agli utenti di esplorare e comprendere i dati in modo efficace e accurato.

