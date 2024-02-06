import pandas as pd
# la classe drop duplicate elimina i campioni che sono presenti più volte all'interno del dataset
class DropDuplicate:
    #il metodo drop riceve in ingresso un dataset e restituisce il dataset senza campioni duplicati
    def drop(self,dataset):
        if dataset.duplicated().any():
            dataset = dataset.drop_duplicates()
            print(dataset)
        return dataset