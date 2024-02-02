import numpy as np
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
        test_index = self.data.index[~self.data.index.isin(train_index)] #  ~ è l'operatore di negazione logica: prende gli indici che non sono in train_index
        #generazione dei train set e test set
        self.train = self.data.loc[train_index] #loc seleziona le righe con gli indici indicati
        self.test = self.data.loc[test_index]
        #generazione dei target
        self.train_target = self.target.loc[train_index]
        self.test_target = self.target.loc[test_index]
        return self.train, self.test, self.train_target, self.test_target

