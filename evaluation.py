import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from manage.holdout import Holdout
from manage.kfoldcrossvalidation import KFoldCrossValidation
from KNNClassifier import KNNClassifier


class Evaluation:
    """
    Modella la valutazione delle performance di un modello.
    """

    def __init__(self, mode, train, test, train_target, test_target):
        """
        Costruttore

        Parameters
        ----------
        mode : str
            la modalità di valutazione
        train : pandas.DataFrame
            il training set
        test : pandas.DataFrame
            il test set
        train_target : pandas.Series
            i valori target del training set
        test_target : pandas.Series
            i valori target del test set

        Returns
            ----
        None

        """

        self.mode = mode
        self.train = train
        self.test = test
        self.train_target = train_target
        self.test_target = test_target

    def choose(self, chosen_method, data, target, K, train_size):
        """
        Sceglie il metodo di valutazione

        Parameters
        ----------
        chosen_method : str
            il metodo di valutazione scelto
        data : pandas.DataFrame
            il dataset
        target : pandas.Series
            i valori target
        K : int
            il numero di fold
        train_size : float
            la percentuale di esempi da assegnare al training set


        Returns
            ----
        None

        """
        if chosen_method == 'holdout':
            holdout_model = Holdout(data, target, train_size)
        elif chosen_method == 'kfold':
            kfold_model = KFoldCrossValidation(data, target, K)
        else:
            print('Errore: metodo di valutazione non riconosciuto')


