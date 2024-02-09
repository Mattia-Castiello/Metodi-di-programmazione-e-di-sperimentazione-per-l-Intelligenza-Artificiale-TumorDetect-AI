import numpy as np
from KNNClassifier import KNNClassifier


class KFoldCrossValidation:
    """
    Modella la tecnica di k-fold cross validation per la suddivisione di un dataset in training set e test set.
    """

    def __init__(self, data, target, K):
        """
        Costruttore

        Parameters
        ----------
        data : pandas.DataFrame
            il dataset da suddividere
        target : pandas.Series
            la serie di valori target
        K : int
            il numero di fold


        Returns
            ----
        None
        """
        self.data = data
        self.target = target
        self.K = K
        self.fold = []


    def split(self):
        """
        Suddivide il dataset in training set e test set.

        Returns
        -------
        list
            una lista di tuple, ognuna delle quali contiene:
            - il training set
            - il test set
            - i valori target del training set
            - i valori target del test set

        """


        indices = np.random.permutation(self.data.index)  # permuta gli indici del dataset
        # generazione dei fold
        fold_size = int(len(self.data) / self.K)
        for i in range(self.K):
            test_index = indices[i * fold_size:(i + 1) * fold_size]  # seleziona gli indici per il test set
            train_index = indices[~np.isin(indices, test_index)]  # isin controlla se è presente quel valore nel DataFrame
            # generazione dei train set e test set
            train = self.data.loc[train_index]  # loc seleziona le righe con gli indici indicati
            test = self.data.loc[test_index]
            # generazione dei target
            train_target = self.target.loc[train_index]
            test_target = self.target.loc[test_index]

            # Trasforma da tupla in una lista
            train = train.values.tolist()
            test = test.values.tolist()
            train_target = train_target.values.tolist()
            test_target = test_target.values.tolist()
            self.fold.append([train, test, train_target, test_target])
        return train, test, train_target, test_target

    def evaluate(self, k):
        """
        Valuta le performance del modello KNN con k-fold cross validation.

        Parameters
        ----------
        k : int
            il valore di k per il modello KNN

        Returns
        -------
        true_positive : list
            il numero di veri positivi
        true_negative : list
            il numero di veri negativi
        false_positive : list
            il numero di falsi positivi
        false_negative : list
            il numero di falsi negativi
        """
        true_positive = []
        true_negative = []
        false_positive = []
        false_negative = []

        for i in range(self.K):
            train, test, train_target, test_target = self.fold[i]
            knn = KNNClassifier(k)
            knn.fit(train, train_target)  # addestra il modello
            predictions = knn.predict(test)  # predice i valori target

            for i in range(len(predictions)):
                if predictions[i] == 1 and test_target[i] == 1:
                    true_positive.append(1)
                elif predictions[i] == 1 and test_target[i] == 0:
                    false_positive.append(1)
                elif predictions[i] == 0 and test_target[i] == 0:
                    true_negative.append(1)
                elif predictions[i] == 0 and test_target[i] == 1:
                    false_negative.append(1)
        return true_positive, true_negative, false_positive, false_negative

    def confusion_matrix(self, true_positive, true_negative, false_positive, false_negative):
        """
        Calcola la matrice di confusione.

        Parameters
        ----------
        true_positive : list
            una lista di int di veri positivi
        true_negative : list
            una lista di int di veri negativi
        false_positive : list
            una lista di int di falsi positivi
        false_negative : list
            una list di int di falsi negativi

        Returns
        -------
        list
            una lista di liste, ognuna dei quali rappresenta i valori della confusion matrix
        """
        confusion_matrix = [true_positive, false_positive, false_negative, true_negative]

        return confusion_matrix

    def accuracy(self, confusion_matrix):
        """
        Calcola l'accuratezza.

        Parameters
        ----------
        confusion_matrix : list
            la confusion matrix

        Returns
        -------
        float
            l'accuratezza
        list
            l'accuratezza scores
        """
        accuracy_scores = []
        for i in range(self.K):
            accuracy_scores.append((confusion_matrix[0] + confusion_matrix[3])/(confusion_matrix[0] + confusion_matrix[1] + confusion_matrix[2] + confusion_matrix[3]))
            accuracy = np.mean(accuracy_scores)
        return accuracy, accuracy_scores

    def error_rate(self, confusion_matrix):
        """
        Calcola l'error rate.

        Parameters
        ----------
        confusion_matrix : list
            la confusion matrix

        Returns
        -------
        float
            l'error rate
        list
            l'error rate scores
        """
        error_rate_scores = []
        for i in range(self.K):
            error_rate_scores.append((confusion_matrix[1] + confusion_matrix[2]) / (confusion_matrix[0] + confusion_matrix[1] + confusion_matrix[2] + confusion_matrix[3]))
            error_rate = np.mean(error_rate_scores)
        return error_rate, error_rate_scores

    def sensitivity(self, confusion_matrix):
        """
        Calcola la sensitivity.

        Parameters
        ----------
        confusion_matrix : list
            la confusion matrix

        Returns
        -------
        float
            la sensitivity
        list
            la sensitivity scores
        """
        sensitivity_scores = []
        for i in range(self.K):
            sensitivity_scores.append(confusion_matrix[3] / (confusion_matrix[3] + confusion_matrix[2]))
            sensitivity = np.mean(sensitivity_scores)
        return sensitivity, sensitivity_scores

    def specificity(self, confusion_matrix):
        """
        Calcola la specificity.

        Parameters
        ----------
        confusion_matrix : list
            la confusion matrix

        Returns
        -------
        float
            la specificity
        list
            la specificity scores
        """
        specificity_scores = []
        for i in range(self.K):
            specificity_scores.append(confusion_matrix[0] / (confusion_matrix[0] + confusion_matrix[1]))
            specificity = np.mean(specificity_scores)
        return specificity, specificity_scores

    def geometric_mean(self, confusion_matrix):
        """
        Calcola la geometric mean.

        Parameters
        ----------
        confusion_matrix : list
            la confusion matrix

        Returns
        -------
        float
            la geometric mean
        list
            la geometric mean
        """
        geometric_mean_scores = []
        for i in range(self.K):
            geometric_mean_scores.append(np.sqrt(self.sensitivity(confusion_matrix) * self.specificity(confusion_matrix)))
            geometric_mean = np.mean(geometric_mean)
        return geometric_mean, geometric_mean_scores
