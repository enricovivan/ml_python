import pandas as pd
import numpy as np
import sklearn.ensemble as sk

class BaggedDecisionTree:

    def __init__(self) -> None:
        
        print('Bagged Decision Tree')

        # Importação do dataset
        self.dataset = pd.read_csv('app/data/Breast_Cancer.csv')

        