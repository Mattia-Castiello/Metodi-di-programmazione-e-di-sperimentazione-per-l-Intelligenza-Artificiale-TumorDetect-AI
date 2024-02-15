import numpy as np
import random

class KNNClassifier:
    def __init__(self, k, weight='None'):
        # Memorizza il valore di k e la misura della distanza come uniforme o distanza
        self.k = k
        self.weight = weight
        self.x_train = None
        self.y_train = None

    def fit(self, x_train, y_train):
        '''
            Addestramento modello KNN con i dati.

            parametri:
            x_train (lista): elenco dei dati di addestramento.
            y_train (lista): elenco delle etichette di addestramento.
        '''
        
        self.x_train = x_train
        self.y_train = y_train
    
    def predict(self, x):
        predictions = []
        for test in x:
            temp = self.__predict(test)
            predictions.append(temp)
        return predictions

    def __predict(self, x):
        distances = []
        for train in self.x_train:
            distance = self.euclidean_distance(x, train)
            distances.append(distance)
        min_distance_indices = sorted(range(len(distances)), key=lambda index: distances[index])[: self.k]
        min_distances = sorted(distances)[: self.k]
        min_distance_labels = []
        for i in min_distance_indices:
            min_distance_labels.append(self.y_train[i][0])  # Prendi solo il primo elemento dall'array

        # Se la misura della distanza non è uniforme, prende la media ponderata dei vicini più prossimi
        if self.weight == 'distance':
            most_common = {}
            for i in range(len(min_distance_labels)):
                current_label = min_distance_labels[i]
                if min_distances[i] != 0:
                    if current_label not in most_common.keys():
                        most_common[current_label] = 1 / min_distances[i]
                    else:
                        most_common[current_label] += 1 / min_distances[i]
            return max(most_common, key=lambda x: most_common[x])
        else:  # Se la misura della distanza è uniforme, prendi la moda dei vicini più prossimi
            most_common = {}
            for i in min_distance_labels:
                if i not in most_common.keys():
                    most_common[i] = 1
                else:
                    most_common[i] += 1
            return max(most_common, key=lambda x: most_common[x])

    def euclidean_distance(self, x, y):
        distance = np.sqrt(np.sum((x-y)**2))
        return distance
