import numpy as np
import joblib
import pandas as pd

class Transformer(object):
    
    def __init__(self):
        self.encoder = joblib.load('CustomerChurnOrdinalEncoder.pkl')
        self.onehotencoder = joblib.load('CustomerChurnOneHotEncoder.pkl')

    def transform_input(self, X, feature_names, meta):
        # print(X)
        # print(feature_names)
        # print(meta)
        df = pd.DataFrame(X, columns=feature_names)
        df = self.encoder.transform(df)
        df = self.onehotencoder.transform(df)
        # print(df.to_numpy())
        return df.to_numpy()


# class Transformer(object):
#     def transform_input(self, X, feature_names, meta):
#         df = pd.DataFrame(X, columns=feature_names)
        
#         #df = df.drop(['customerID'], axis=1)
#         return df.to_numpy()
