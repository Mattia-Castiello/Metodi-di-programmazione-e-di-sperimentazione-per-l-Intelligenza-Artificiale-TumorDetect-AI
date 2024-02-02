import pandas as pd

class Bridge:
    def impution(self,dataset):
        if dataset.isnull().sum().any():
            col_Nan = dataset.columns[dataset.isnull().sum() > 0].tolist()
            print(col_Nan)

            for col in col_Nan:
                revenue = dataset[col]
                revenue_mean = revenue.median()
                dataset[col].fillna(revenue_mean, inplace=True)
            return dataset
        return dataset
