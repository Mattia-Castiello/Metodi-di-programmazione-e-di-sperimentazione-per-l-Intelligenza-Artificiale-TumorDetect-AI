import pandas as pd

class Duplicate:
    def drop(self,dataset):
        if dataset.duplicated().any():
            dataset = dataset.drop_duplicates()
            print(dataset)
        return dataset