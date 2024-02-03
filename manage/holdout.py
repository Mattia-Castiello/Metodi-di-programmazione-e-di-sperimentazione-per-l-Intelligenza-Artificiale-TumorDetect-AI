import numpy as np
from KNNClassifier import KNNClassifier
class Holdout:
    """
    Modella la tecnica di holdout per la suddivisione di un dataset in training set e test set.
    """
    def __init__(self, data, target, train_size=0.8):
        """
        Costruttore

        Parameters
        ----------
        data : pandas.DataFrame
            il dataset da suddividere
        target : pandas.Series
            la serie di valori target
        train_size : float, optional
            la proporzione di esempi da assegnare al training set. Di default è 0.8.


        Returns
            ----
        None
        """
        self.data = data
        self.target = target
        self.train_size = train_size
        self.train = None
        self.test = None
        self.train_target = None
        self.test_target = None

    def split(self):
        """
        Suddivide il dataset in training set e test set.

        Returns
        -------
        pandas.DataFrame
            il training set
        pandas.DataFrame
            il test set
        pandas.Series
            i valori target del training set
        pandas.Series
            i valori target del test set

        """

        train_index = np.random.choice(self.data.index, size=int(self.train_size*len(self.data)), replace=False)
        test_index = self.data.index[~self.data.index.isin(train_index)] # ~ è l'operatore di negazione logica: prende gli indici che non sono in train_index. isin controlla se è presente quel valore nel DataFrame
        #generazione dei train set e test set
        self.train = self.data.loc[train_index] #loc seleziona le righe con gli indici indicati
        self.test = self.data.loc[test_index]
        #generazione dei target
        self.train_target = self.target.loc[train_index]
        self.test_target = self.target.loc[test_index]

        #conversione da dataframe a lista
        self.train = self.train.values.tolist()
        self.test = self.test.values.tolist()
        self.train_target = self.train_target.values.tolist()
        self.test_target = self.test_target.values.tolist()
        return self.train, self.test, self.train_target, self.test_target

    def evaluate(self):
        """
        Valuta il modello.

        Returns
        -------
        true_positive : int
            il numero di veri positivi
        false_positive : int
            il numero di falsi positivi
        true_negative : int
            il numero di veri negativi
        false_negative : int
            il numero di falsi negativi


        """
        knn = KNNClassifier(3)
        knn.fit(self.train, self.train_target) #addestra il modello
        predictions = knn.predict(self.test) #predice i valori target

        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0

        for i in range(len(predictions)):
            if predictions[i] == self.test_target[i]:
                true_positive += 1
            else:
                false_positive += 1
            if predictions[i] != self.test_target[i]:
                true_negative += 1
            else:
                false_negative += 1
        return true_positive, false_positive, true_negative, false_negative


    def confusion_matrix(self, true_positive, false_positive, true_negative, false_negative):
        """
        Calcola la confusion matrix.

        Parameters
        ----------
        true_positive : int
            il numero di veri positivi
        false_positive : int
            il numero di falsi positivi
        true_negative : int
            il numero di veri negativi
        false_negative : int
            il numero di falsi negativi

        Returns
        -------
        list
            la confusion matrix

        """
        confusion_matrix = [true_negative, false_positive, false_negative, true_positive]
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

        accuracy = (confusion_matrix[0] + confusion_matrix[3]) / (confusion_matrix[0] + confusion_matrix[1] + confusion_matrix[2] + confusion_matrix[3])
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
        error_rate = (confusion_matrix[1] + confusion_matrix[2]) / (confusion_matrix[0] + confusion_matrix[1] + confusion_matrix[2] + confusion_matrix[3])
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
