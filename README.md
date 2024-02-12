# Progetto_Progammazione_23-24
Questo progetto ha lo scopo di sviluppare un programma che, ricevendo in ingresso un dataset contenente informazioni su alcuni tipi di cellule tumorali, sappia determinare se un tumore è benigno o maligno. Il programma utilizza un classificatore k-NN (k-Nearest Neighbors) per classificare i dati e valutare le prestazioni del modello. Le tecniche di valutazione implementate sono `Holdout` e `K-Fold Cross Validation` e possono essere selezionate dall'utente. L'obiettivo finale è quello di testare le prestazioni del modello e valutarne le performance mediante metriche e grafici che verranno salvati in un file di output. Il programma è stato sviluppato in modo da essere flessibile e personalizzabile, consentendo all'utente di specificare le opzioni di input e di personalizzare l'analisi in base alle proprie esigenze.



# Il Dataset 
Nel contesto di questo progetto, utilizziamo il dataset `breast_cancer.csv` il quale fornisce dettagli su alcuni tipi di cellule tumorali. Il dataset è strutturato come segue:

- **Numero di Campioni**: 683 campioni.

- **Numero di Caratteristiche**: 11 caratteristiche per campione.

- **Nomi delle Caratteristiche**:

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
Per eseguire il codice, è necessario seguire i seguenti passaggi:

- **Installazione dei Requisiti**: prima di avviare l'applicazione, è indispensabile installare i requisiti. Questo può essere realizzato eseguendo il comando `pip install -r requirements.txt` nella cartella principale del progetto. Questo comando installerà tutte le librerie richieste: numpy, pandas, matplotlib ed altre.

- **Importazione del Dataset**: Il dataset `breast_cancer.csv` è già presente nel repository e pronto per l'uso. Tuttavia, se si desidera utilizzare un dataset diverso, è possibile caricare un file CSV di input che contiene il dataset. L'applicazione è in grado di gestire file CSV e JSON.

- **Impostazione delle Opzioni di Input**: L'applicazione offre diverse opzioni di input per personalizzare l'esecuzione e l'analisi:

  - `File di input`: Puoi indicare il percorso di un file CSV o JSON di input che contiene il dataset. Nel caso in cui l'estensione del file non sia .csv o .json, l'applicazione chiederà di inserire un file valido.

  - `Numero di vicini (k)` da utilizzare nel classificatore k-NN: Questo parametro influisce su come il modello classifica i nuovi dati basandosi sui dati di addestramento.
  - `Metodo di valutazione`: Puoi scegliere tra Holdout e K-fold Cross Validation. Queste opzioni determinano come vengono valutate le performance del modello.
    - **Holdout**: Questo metodo divide il dataset in due parti: una parte per l'addestramento e una parte per il test. Questo metodo è utile quando si dispone di un grande dataset.
    - **K-fold Cross Validation**: Questo metodo divide il dataset in k fold e utilizza k-1 fold per l'addestramento e 1 fold per il test. Questo metodo è utile quando si dispone di un piccolo dataset.
  - `Percentuale di test`: Questo parametro determina la percentuale di dati da utilizzare per il test. Questo valore è utilizzato solo se si sceglie Holdout come metodo di valutazione.
  - `Numero di fold`: Questo parametro determina il numero di fold da utilizzare. Questo valore è utilizzato solo se si sceglie K-fold Cross Validation come metodo di valutazione.
  - `Metriche di valutazione`: Determinano il modo in cui vengono valutate le performance del modello. Sono disponibili le seguenti metriche:
    - **Accuracy Rate**: Indica quante volte il nostro modello ha correttamente classificato correttamente un item nel nel nostro dataset rispetto al totale
    - **Error Rate(TPR)**: Indica quante volte il nostro modello ha erroneamente classificato correttamente un item nel nel nostro dataset rispetto al totale
    - **Sensitivity**: Indica la capacità del modello di individuare i casi positivi correttamente.
    - **Specificity(TNR)**: Indica la capacità del modello di individuare i casi negativi corretamente.
    - **Geometric Mean**: Misura l'equilibrio tra Sensibilità e Specificità.
  - `Nome del file di output`: Puoi specificare il nome del file di output in cui salvare i risultati dell'analisi. Se non viene specificato alcun nome, l'applicazione utilizzerà un nome predefinito.

- **Esecuzione del programma**: Il programma può essere eseguito tramite il file `main.py`, specificando le opzioni di input come argomenti della linea di comando, quando e come richiesto.

# Risultati
I risultati dell'esecuzione del programma sono presentati in due modi:
1) Se si sceglie come metodo di valutazione `Holdout` si otterrà un file di output con il nome desiderato o, di default, `Metrics.txt`, nel quale sono salvate le metriche di validazione del modello.
2) Se si sceglie come metodo di valutazione `K-fold Cross Validation` si otterrà un file di output con il nome desiderato o, di default, `Metrics.txt`, dove sono salvate le metriche di validazione del modello, e due plot:
   - 2.1 `Boxplot`: per ciascuna metrica mostra la distribuzione dei valori in tutti gli esperimenti.
   - 2.2 `Line Plot`: illustra per ciascuna metrica come i valori cambiano attraverso diversi esperimenti.

# Configurazione del virtual environment
Prima di eseguire il programma, è necessario configurare un virtual environment. Questo può essere realizzato eseguendo i comandi:
1) Creare un virtual environment da terminale:
   - `python3 -m venv venv`
2) Attivare il virtual environment:
   - **Windows**: `.\venv\Scripts\activate`
   - **Unix/MacOS**: `source .\venv/bin/activate`
3) Installare i requisiti:
   - `pip install -r requirements.txt`


