import pandas as pd
import numpy as np
import sklearn.ensemble as sk
from dataprep.eda import create_report

class RandomForest:

    def __init__(self) -> None:
        
        print('Bagged Decision Tree')

        # Importação do Dataset
        self.data = pd.read_csv('app/data/Breast_Cancer.csv')

        # Verificar Linhas Duplicadas
        print(self.data.duplicated())

        

        