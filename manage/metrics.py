import numpy as np
import matplotlib.pyplot as plt

class Metrics:
    """
    Modella le metriche di validazione del modello
    """
    def __init__(self, true_positive, true_negative, false_positive, false_negative, metrics=[]):
        """
        Costruttore

        Parameters
        ----------
        true_positive : int
            il numero di veri positivi
        true_negative : int
            il numero di veri negativi
        false_positive : int
            il numero di falsi positivi
        false_negative : int
            il numero di falsi negativi
        metrics : list
            la lista delle metriche

        Returns
        -------
        None
        """
        self.true_positive = true_positive
        self.true_negative = true_negative
        self.false_positive = false_positive
        self.false_negative = false_negative
        self.metrics = metrics

    def confusion_matrix(self):
        """
        Calcola la confusion matrix

        Returns
        -------
        list
            la confusion matrix
        """
        print("True Positive: ", self.true_positive)
        print("True Negative: ", self.true_negative)
        print("False Positive: ", self.false_positive)
        print("False Negative: ", self.false_negative)
        confusion_matrix = [self.true_negative, self.false_positive, self.false_negative, self.true_positive]
        print("confusion matrix: ", confusion_matrix)

        return confusion_matrix

    def accuracy(self, confusion_matrix, K=1):
        """
        Calcola l'accuratezza

        Parameters
        ----------
        confusion_matrix : list
            la confusion matrix

        K : int
            il numero di esperimenti
        Returns
        -------
        accuracy : float
            l'accuratezza

        accuracy scores: list
            i valori di accuratezza per ogni esperimento

        """
        accuracy_scores = []
        true_positive = confusion_matrix[0]
        false_positive = confusion_matrix[1]
        false_negative = confusion_matrix[2]
        true_negative = confusion_matrix[3]
        # Se la confusion matrix è una lista di liste
        if isinstance(confusion_matrix[0], list):
            for i in range(K):
                accuracy_scores.append((true_positive[i] + true_negative[i]) / (true_positive[i] + false_positive[i] + false_negative[i] + true_negative[i]))
        # Se la confusion matrix è una lista singola
        else:
            accuracy_scores.append((true_positive + true_negative) / (true_positive + false_positive + false_negative + true_negative))

        accuracy = np.mean(accuracy_scores)
        return accuracy, accuracy_scores

    def error_rate(self, confusion_matrix, K=1):
        """
        Calcola l'error rate

        Parameters
        ----------
        confusion_matrix : list
            la confusion matrix

        K : int
            il numero di esperimenti
        Returns
        -------
        error_rate : float
            l'error rate

        error_rate_scores : list
            i valori di error rate per ogni esperimento

        """
        error_rate_scores = []
        true_positive = confusion_matrix[0]
        false_positive = confusion_matrix[1]
        false_negative = confusion_matrix[2]
        true_negative = confusion_matrix[3]
        # Se la confusion matrix è una lista di liste
        if isinstance(confusion_matrix[0], list):
            for i in range(K):
                error_rate_scores.append((false_positive[i] + false_negative[i]) / (true_positive[i] + false_positive[i] + false_negative[i] + true_negative[i]))
        # Se la confusion matrix è una lista singola
        else:
            error_rate_scores.append((false_positive + false_negative) / (true_positive + false_positive + false_negative + true_negative))
        error_rate = np.mean(error_rate_scores)
        return error_rate, error_rate_scores

    def sensitivity(self, confusion_matrix, K=1):
        """
        Calcola la sensitivity

        Parameters
        ----------
        confusion_matrix : list
            la confusion matrix

        K : int
            il numero di esperimenti
        Returns
        -------
        sensitivity : float
            la sensitivity

        sensitivity_scores : list
            i valori di sensitivity per ogni esperimento

        """
        sensitivity_scores = []
        true_positive = confusion_matrix[0]
        false_positive = confusion_matrix[1]
        false_negative = confusion_matrix[2]
        true_negative = confusion_matrix[3]

        # Se la confusion matrix è una lista di liste
        if isinstance(confusion_matrix[0], list):
            for i in range(K):
                sensitivity_scores.append(true_positive[i] / (true_positive[i] + false_negative[i]))
        # Se la confusion matrix è una lista singola
        else:
            sensitivity_scores.append(true_positive / (true_positive + false_negative))

        sensitivity = np.mean(sensitivity_scores)
        return sensitivity, sensitivity_scores

    def specificity(self, confusion_matrix, K=1):
        """
        Calcola la specificity

        Parameters
        ----------
        confusion_matrix : list
            la confusion matrix

        K : int
            il numero di esperimenti
        Returns
        -------
        specificity : float
            la specificity

        specificity_scores : list
            i valori di specificity per ogni esperimento

        """
        specificity_scores = []
        true_positive = confusion_matrix[0]
        false_positive = confusion_matrix[1]
        false_negative = confusion_matrix[2]
        true_negative = confusion_matrix[3]

        # Se la confusion matrix è una lista di liste
        if isinstance(confusion_matrix[0], list):
            for i in range(K):
                specificity_scores.append(true_negative[i] / (true_negative[i] + false_positive[i]))
        # Se la confusion matrix è una lista singola
        else:
            specificity_scores.append(true_negative / (true_negative + false_positive))
        specificity = np.mean(specificity_scores)
        return specificity, specificity_scores

    def geometric_mean(self, confusion_matrix, K=1):
        """
        Calcola la geometric mean

        Parameters
        ----------
        confusion_matrix : list
            la confusion matrix

        K : int
            il numero di esperimenti
        Returns
        -------
        geometric_mean : float
            la geometric mean

        geometric_mean_scores : list
            i valori di geometric mean per ogni esperimento

        """
        geometric_mean_scores = []
        true_positive = confusion_matrix[0]
        false_positive = confusion_matrix[1]
        false_negative = confusion_matrix[2]
        true_negative = confusion_matrix[3]

        # Se la confusion matrix è una lista di liste
        if isinstance(confusion_matrix[0], list):
            for i in range(K):
                sensitivity = true_positive[i] / (true_positive[i] + false_negative[i])
                specificity = true_negative[i] / (true_negative[i] + false_positive[i])
                geometric_mean_scores.append(np.sqrt(sensitivity * specificity))
        # Se la confusion matrix è una lista singola
        else:
            sensitivity = true_positive / (true_positive + false_negative)
            specificity = true_negative / (true_negative + false_positive)
            geometric_mean_scores.append(np.sqrt(sensitivity * specificity))
        geometric_mean = np.mean(geometric_mean_scores)
        return geometric_mean, geometric_mean_scores


    def get_metrics(self, K=1):
        """
        Calcola tutte le metriche

        Parameters
        ----------

        K : int
            il numero di esperimenti
        Returns
        -------
        list
            le metriche
        """
        metrics = {}
        confusion_matrix = self.confusion_matrix()
        if 1 in self.metrics:
            metrics['Accuracy'] = self.accuracy(confusion_matrix, K)
        if 2 in self.metrics:
            metrics['Error Rate'] = self.error_rate(confusion_matrix, K)
        if 3 in self.metrics:
            metrics['Sensitivity'] = self.sensitivity(confusion_matrix, K)
        if 4 in self.metrics:
            metrics['Specificity'] = self.specificity(confusion_matrix, K)
        if 5 in self.metrics:
            metrics['Geometric Mean'] = self.geometric_mean(confusion_matrix, K)
        if 6 in self.metrics:
            metrics = {
                'Accuracy': self.accuracy(confusion_matrix, K),
                'Error Rate': self.error_rate(confusion_matrix, K),
                'Sensitivity': self.sensitivity(confusion_matrix, K),
                'Specificity': self.specificity(confusion_matrix, K),
                'Geometric Mean': self.geometric_mean(confusion_matrix, K)
            }
        return metrics

    def save_metrics(self, metrics, filename='Metrics.txt'):
        """
        Salva le metriche su file

        Parameters
        ----------
        metrics : dict
            le metriche

        filename : str
            il nome del file
        Returns
        -------
        None
        """
        with open(filename, 'w') as file:
            for metric, value in metrics.items():
                # Verifica se il valore è una lista
                if isinstance(value, list):
                    # Se è una lista, formatta la lista come stringa
                    value_str = ', '.join([str(v) for v in value])
                    print(f'{metric}: {value_str}')
                    file.write(f'{metric}: {value_str}\n')
                else:
                    file.write(f'{metric}: {value[1]}\n')
        print("Le metriche sono state salvate su file.")
        return None

    def metrics_plot(self, metrics):
        """
        Mostra i grafici delle metriche

        Parameters
        ----------
        accuracy_scores : list
            i valori di accuratezza per ogni esperimento

        error_rate_scores : list
            i valori di error rate per ogni esperimento

        sensitivity_scores : list
            i valori di sensitivity per ogni esperimento

        specificity_scores : list
            i valori di specificity per ogni esperimento

        geometric_mean_scores : list
            i valori di geometric mean per ogni esperimento
        Returns
        -------
        None
        """
        # Estraiamo le etichette delle metriche
        labels = list(metrics.keys())
        # Estraiamo le liste dei valori delle metriche
        metric_scores = [value[1] for value in metrics.values()]

        # Plot del boxplot
        plt.figure(figsize=(12, 6))
        plt.boxplot(metric_scores, labels=labels)

        plt.xlabel('Metriche')  # Asse x
        plt.ylabel('Valori')  # Asse y
        plt.title('Metriche di validazione')  # Titolo del grafico
        plt.grid(True)  # Mostra la griglia

        # Estrazione dei dati per il plot a linea
        K_experiments = list(range(1, len(metric_scores[0]) + 1))

        # Plot per ciascuna metrica
        plt.figure(figsize=(12, 6))
        # Plot per ciascuna metrica
        for label, values in zip(labels, metric_scores):
            plt.plot(K_experiments, values, marker='o', label=label)

        # Etichette e titoli
        plt.xlabel('Esperimento K')
        plt.ylabel('Valore della metrica')
        plt.title('Andamento delle metriche negli esperimenti K')

        # Mostra la legenda
        plt.legend()

        # Mostra il grafico
        plt.grid(True)
        plt.show()




