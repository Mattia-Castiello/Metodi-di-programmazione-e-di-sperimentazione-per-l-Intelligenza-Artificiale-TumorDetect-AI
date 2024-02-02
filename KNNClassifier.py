import numpy as np

class ClassificatoreKNN:
    def __init__(self, k, peso=None):
        self.k = k
        self.peso = peso  # Peso per la predizione

    def addestra(self, x_addestramento, y_addestramento):
        '''
            Addestramento modello KNN con i dati.

            parametri:
            x_addestramento (lista): elenco dei dati di addestramento.
            y_addestramento (lista): elenco delle etichette di addestramento.
            k =
            peso  # Peso per la predizione
        '''
        
        self.x_addestramento = x_addestramento
        self.y_addestramento = y_addestramento

    def predizione(self, X):
        predizioni = []
        for test in X:
            temp = self.__predizione(test)
            predizioni.append(temp)
        return predizioni

    def __predizione(self, x):
        distanze = []
        for addestramento in self.x_addestramento:
            distanza = self.distanza_euclidea(x, addestramento)
            distanze.append(distanza)
        indici_distanze_minime = sorted(range(len(distanze)), key=lambda indice: distanze[indice])[:self.k]
        distanze_minime = sorted(distanze)[:self.k]
        print(indici_distanze_minime)
        etichette_distanze_minime = []
        for i in indici_distanze_minime:
            etichette_distanze_minime.append(self.y_addestramento[i])
        
        if self.peso == 'distanza':
            piu_comuni = {}
            for i in range(len(etichette_distanze_minime)):
                etichetta_corrente = etichette_distanze_minime[i]
                if distanze_minime[i] != 0:
                    if etichetta_corrente not in piu_comuni.keys():
                        piu_comuni[etichetta_corrente] = 1/distanze_minime[i]
                    else:
                        piu_comuni[etichetta_corrente] += 1/distanze_minime[i]
            return max(piu_comuni, key=lambda x: piu_comuni[x])
        else:
            piu_comuni = {}
            for i in etichette_distanze_minime:
                if i not in piu_comuni.keys():
                    piu_comuni[i] = 1
                else:
                    piu_comuni[i] += 1
            return max(piu_comuni, key=lambda x: piu_comuni[x])

    def distanza_euclidea(self, x, y):
        distanza = np.sqrt(np.sum(x-y)**2)
        return distanza
