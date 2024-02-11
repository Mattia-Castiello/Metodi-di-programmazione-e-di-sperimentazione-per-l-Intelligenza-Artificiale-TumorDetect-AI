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
        for i in range(K):
            accuracy_scores.append((confusion_matrix[0] + confusion_matrix[3])/(confusion_matrix[0] + confusion_matrix[1] + confusion_matrix[2] + confusion_matrix[3]))
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
        for i in range(K):
            error_rate_scores.append((confusion_matrix[1] + confusion_matrix[2])/(confusion_matrix[0] + confusion_matrix[1] + confusion_matrix[2] + confusion_matrix[3]))
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
        for i in range(K):
            sensitivity_scores.append(confusion_matrix[0]/(confusion_matrix[0] + confusion_matrix[2]))
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
        for i in range(K):
            specificity_scores.append(confusion_matrix[3]/(confusion_matrix[3] + confusion_matrix[1]))
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
        for i in range(K):
            sensitivity = confusion_matrix[0]/(confusion_matrix[0] + confusion_matrix[2])
            specificity = confusion_matrix[3]/(confusion_matrix[3] + confusion_matrix[1])
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
                file.write(f'{metric}: {value}\n')
        print("Le metriche sono state salvate su file.")
        return None

    def metrics_plot(self, accuracy_scores, error_rate_scores, sensitivity_scores, specificity_scores, geometric_mean_scores):
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
        label = ['Accuracy', 'Error Rate', 'Sensitivity', 'Specificity', 'Geometric Mean']
        values = [accuracy_scores, error_rate_scores, sensitivity_scores, specificity_scores, geometric_mean_scores]

        plt.figure(figsize=(10, 10))
        plt.boxplot(values, labels=label)

        plt.legend(loc='upper left') #posiziona la legenda in alto a sinistra
        plt.xlabel('Esperimenti') #asse x
        plt.ylabel('Metriche') #asse y
        plt.title('Metriche di validazione') #titolo del grafico
        plt.show()





