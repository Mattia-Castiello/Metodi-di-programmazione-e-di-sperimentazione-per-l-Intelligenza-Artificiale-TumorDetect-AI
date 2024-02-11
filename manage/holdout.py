import numpy as np
from KNNClassifier import KNNClassifier
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
        train_size : float, optional
            la proporzione di esempi da assegnare al training set. Di default è 0.8.


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
        test_index = self.data.index[~self.data.index.isin(train_index)] # ~ è l'operatore di negazione logica: prende
        # gli indici che non sono in train_index.
        # isin controlla se è presente quel valore nel DataFrame

        #generazione dei train set e test set
        train = self.data.loc[train_index] #loc seleziona le righe con gli indici indicati
        test = self.data.loc[test_index]
        #generazione dei target
        train_target = self.target.loc[train_index]
        test_target = self.target.loc[test_index]

        print("\nlunghezze train e test: ", len(train), len(test), len(train_target), len(test_target))
        return train, test, train_target, test_target



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
        train, test, train_target, test_target = self.split()
        train = train.to_numpy()
        train_target = train_target.to_numpy()
        test = test.to_numpy()
        test_target = test_target.to_numpy()
        print("split type: ", type(train), type(test), type(train_target), type(test_target))

        knn = KNNClassifier(self.k, self.weight)
        knn.fit(train, train_target) #addestra il modello
        predictions = knn.predict(test) #predice i valori target

        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0

        print("predictions len: ", len(predictions), "\ntest_target len: ", len(test_target))
        print("predictions: ", predictions)

        for i in range(len(predictions)):
            if predictions[i] == 4 and test_target[i] == 4:
                true_positive += 1
            elif predictions[i] == 4 and test_target[i] == 2:
                false_positive += 1
            elif predictions[i] == 2 and test_target[i] == 2:
                true_negative += 1
            elif predictions[i] == 2 and test_target[i] == 4:
                false_negative += 1

        return true_positive, false_positive, true_negative, false_negative



