import pandas as pd
import numpy as np
class Standardization:
    def standardizer(self,dataset):
        for col in dataset.columns:
            if np.issubdtype(dataset[col].dtype,np.number) and col != 'Class' and col!= 'Sample code number':
                std = dataset[col].std()
                mean = dataset[col].mean()
                dataset[col] = (dataset[col] - mean) / std
                print(dataset)

        return dataset