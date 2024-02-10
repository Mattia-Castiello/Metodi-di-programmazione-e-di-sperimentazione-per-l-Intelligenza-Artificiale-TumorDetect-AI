import numpy as np
from Input import Input

class Metrics:
    """
    Modella le metriche di validazione del modello
    """
    def __init__(self, true_positive, true_negative, false_positive, false_negative):
        """
        Costruttore

        Parameters
        ----------
        true_positive : list
            il numero di veri positivi
        true_negative : list
            il numero di veri negativi
        false_positive : list
            il numero di falsi positivi
        false_negative : list
            il numero di falsi negativi

        Returns
        -------
        None
        """
        self.true_positive = true_positive
        self.true_negative = true_negative
        self.false_positive = false_positive
        self.false_negative = false_negative

    def confusion_matrix(self):
        """
        Calcola la confusion matrix

        Returns
        -------
        list
            la confusion matrix
        """
        confusion_matrix = [len(self.true_negative), len(self.false_positive), len(self.false_negative), len(self.true_positive)]
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
        float
            l'accuratezza

        list
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
        float
            l'error rate

        list
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
        float
            la sensitivity

        list
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
        float
            la specificity

        list
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
        float
            la geometric mean

        list
            i valori di geometric mean per ogni esperimento

        """
        geometric_mean_scores = []
        for i in range(K):
            sensitivity = confusion_matrix[0]/(confusion_matrix[0] + confusion_matrix[2])
            specificity = confusion_matrix[3]/(confusion_matrix[3] + confusion_matrix[1])
            geometric_mean_scores.append(np.sqrt(sensitivity * specificity))
            geometric_mean = np.mean(geometric_mean_scores)
        return geometric_mean, geometric_mean_scores


    def get_metrics(self, confusion_matrix, K=1):
        """
        Calcola tutte le metriche

        Parameters
        ----------
        confusion_matrix : list
            la confusion matrix

        K : int
            il numero di esperimenti
        Returns
        -------
        list
            le metriche
        """
        metrics = []
        if 1 in Input.choose_metrics:
            metrics.append(self.accuracy(confusion_matrix, K))
        if 2 in Input.choose_metrics:
            metrics.append(self.error_rate(confusion_matrix, K))
        if 3 in Input.choose_metrics:
            metrics.append(self.sensitivity(confusion_matrix, K))
        if 4 in Input.choose_metrics:
            metrics.append(self.specificity(confusion_matrix, K))
        if 5 in Input.choose_metrics:
            metrics.append(self.geometric_mean(confusion_matrix, K))
        if 6 in Input.choose_metrics:
            metrics = [self.accuracy(confusion_matrix, K), self.error_rate(confusion_matrix, K), self.sensitivity(confusion_matrix, K), self.specificity(confusion_matrix, K), self.geometric_mean(confusion_matrix, K)]
        return metrics

    def save_metrics(self, metrics, filename='Metrics.txt'):
        """
        Salva le metriche su file

        Parameters
        ----------
        metrics : list
            le metriche

        filename : str
            il nome del file
        Returns
        -------
        None
        """
        with open(filename, 'w') as file:
            for metric in metrics:
                file.write(str(metric) + '\n')
        print("Le metriche sono state salvate su file.")
        return None




