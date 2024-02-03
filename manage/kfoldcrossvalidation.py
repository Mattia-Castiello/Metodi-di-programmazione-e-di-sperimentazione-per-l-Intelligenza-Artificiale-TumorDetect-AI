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
            train_index = indices[
                ~np.isin(indices, test_index)]  # isin controlla se è presente quel valore nel DataFrame
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
        true_positive : int
            il numero di veri positivi
        true_negative : int
            il numero di veri negativi
        false_positive : int
            il numero di falsi positivi
        false_negative : int
            il numero di falsi negativi
        """
        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0

        for i in range(self.K):
            train, test, train_target, test_target = self.fold[i]
            knn = KNNClassifier(k)
            knn.fit(train, train_target)  # addestra il modello
            predictions = knn.predict(test)  # predice i valori target
            correct = 0  # contatore per il numero di predizioni corrette
            for i in range(len(predictions)):
                if predictions[i] == test_target[i]:
                    true_positive += 1
                else:
                    false_positive += 1
                if predictions[i] != test_target[i]:
                    false_negative += 1
                else:
                    true_negative += 1
        return true_positive, true_negative, false_positive, false_negative

    def confusion_matrix(self, true_positive, true_negative, false_positive, false_negative):
        """
        Calcola la matrice di confusione.

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

        Returns
        -------
        list
            una lista di float, ognuno dei quali rappresenta i valori della confusion matrix
        """
        confusion_matrix = []
        confusion_matrix.append(true_negative)
        confusion_matrix.append(false_positive)
        confusion_matrix.append(false_negative)
        confusion_matrix.append(true_positive)
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
        """
        accuracy = (confusion_matrix[0] + confusion_matrix[3]) / (
                    confusion_matrix[0] + confusion_matrix[1] + confusion_matrix[2] + confusion_matrix[3])
        return accuracy

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
        """
        error_rate = (confusion_matrix[1] + confusion_matrix[2]) / (
                    confusion_matrix[0] + confusion_matrix[1] + confusion_matrix[2] + confusion_matrix[3])
        return error_rate

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
        """
        sensitivity = confusion_matrix[3] / (confusion_matrix[3] + confusion_matrix[2])
        return sensitivity

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
        """
        specificity = confusion_matrix[0] / (confusion_matrix[0] + confusion_matrix[1])
        return specificity

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
        """
        geometric_mean = np.sqrt(self.sensitivity(confusion_matrix) * self.specificity(confusion_matrix))
        return geometric_mean
