import numpy as np
from KNNClassifier import KNNClassifier
from manage.metrics import Metrics
class Holdout:
    """
    Modella la tecnica di holdout per la suddivisione di un dataset in training set e test set.
    """
    def __init__(self, data, target, metrics, k, weight, train_size=0.8):
        """
        Costruttore

        Parameters
        ----------
        data : pandas.DataFrame
            il dataset da suddividere
        target : pandas.Series
            la serie di valori target
        metrics : list
            la lista di metriche da calcolare
        k : int
            il valore di k per il modello KNN
        weight : string
            il metodo di pesatura da utilizzare
        train_size : float
            la percentuale di dati da utilizzare nel training set

        Returns
            ----
        None
        """
        self.data = data
        self.target = target
        self.metrics = metrics
        self.k = k
        self.weight = weight
        self.train_size = train_size
        self.metrics = metrics


    def split(self):
        """
        Suddivide il dataset in training set e test set.

        Returns
        -------
        train : numpy.ndarray
            il training set
        test : numpy.ndarray
            il test set
        train_target : numpy.ndarray
            i valori target del training set
        test_target : numpy.ndarray
            i valori target del test set

        """

        train_index = np.random.choice(self.data.index, size=int(self.train_size*len(self.data)), replace=False)
        test_index = self.data.index[~self.data.index.isin(train_index)]

        # generazione dei train set e test set
        train = self.data.loc[train_index]
        test = self.data.loc[test_index]
        # generazione dei target
        train_target = self.target.loc[train_index]
        test_target = self.target.loc[test_index]

        # conversione in Numpy array
        train = train.to_numpy()
        train_target = train_target.to_numpy()
        test = test.to_numpy()
        test_target = test_target.to_numpy()

        return train, test, train_target, test_target


    def evaluate(self):
        """
        Valuta il modello.

        Returns
        -------
        None

        """
        # suddividisione del dataset
        train, test, train_target, test_target = self.split()

        # creazione di un'istanza del modello KNN
        knn = KNNClassifier(self.k, self.weight)

        # addestramento del modello
        knn.fit(train, train_target)
        # predizione dei valori target
        predictions = knn.predict(test)

        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0

        # calcolo le metriche
        for i in range(len(predictions)):
            if predictions[i] == 4 and test_target[i] == 4:
                true_positive += 1
            elif predictions[i] == 4 and test_target[i] == 2:
                false_positive += 1
            elif predictions[i] == 2 and test_target[i] == 2:
                true_negative += 1
            elif predictions[i] == 2 and test_target[i] == 4:
                false_negative += 1

        metrics = Metrics(true_positive, true_negative, false_positive, false_negative, self.metrics)
        output_metrics = metrics.get_metrics()
        metrics.save_metrics(output_metrics)
