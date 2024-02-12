import numpy as np
from KNNClassifier import KNNClassifier
from manage.metrics import Metrics


class KFoldCrossValidation:
    """
    Modella la tecnica di k-fold cross validation per la suddivisione di un dataset in training set e test set.
    """

    def __init__(self, data, target, metrics, k,weight, K, fold=[]):
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
        self.metrics = metrics
        self.k = k
        self.weight = weight
        self.K = K
        self.fold = fold


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

            # converte i DataFrame e le Series in array numpy
            train = train.to_numpy()
            test = test.to_numpy()
            train_target = train_target.to_numpy()
            test_target = test_target.to_numpy()

            self.fold.append([train, test, train_target, test_target])
        return self.fold

    def evaluate(self):
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
        true_positive_list= []
        true_negative_list = []
        false_positive_list = []
        false_negative_list = []
        self.split()

        for i in range(self.K):
            train, test, train_target, test_target = self.fold[i]
            print("split type: ", type(train), type(test), type(train_target), type(test_target))
            knn = KNNClassifier(self.k, self.weight)
            knn.fit(train, train_target)  # addestra il modello
            predictions = knn.predict(test)  # predice i valori target

            true_positive = 0
            true_negative = 0
            false_positive = 0
            false_negative = 0
            for i in range(len(predictions)):
                if predictions[i] == 4 and test_target[i] == 4:
                    true_positive += 1
                elif predictions[i] == 4 and test_target[i] == 2:
                    false_positive += 1
                elif predictions[i] == 2 and test_target[i] == 2:
                    true_negative += 1
                elif predictions[i] == 2 and test_target[i] == 4:
                    false_negative += 1
            true_positive_list.append(true_positive)
            true_negative_list.append(true_negative)
            false_positive_list.append(false_positive)
            false_negative_list.append(false_negative)
        print("true positive list: ", true_positive_list, "\ntrue negative list: ", true_negative_list,
              "\nfalse positive list: ", false_positive_list, "\nfalse negative list: ", false_negative_list)

        metrics = Metrics(true_positive_list, true_negative_list, false_positive_list, false_negative_list,self.metrics)
        output_metrics = metrics.get_metrics(self.K)
        metrics.save_metrics(output_metrics)
        metrics.metrics_plot(output_metrics)

