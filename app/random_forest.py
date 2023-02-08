import pandas as pd
import numpy as np
import sklearn.ensemble as sk
from dataprep.eda import create_report
from matplotlib import pyplot as plt
import seaborn as sns

class RandomForest:

    def __init__(self) -> None:
        
        print('\nBagged Decision Tree\n')

        # Importação do Dataset
        self.data = pd.read_csv('app/data/Breast_Cancer.csv')

        # Verificar Linhas Duplicadas e Valores Nulos
        print(f'Quantidade de Dados Duplicados: \n{self.data.duplicated().sum()}\n')
        print(f'Valores Nulos: \n{self.data.isnull().sum()}')

        # Neste caso existe uma linha duplicada, faremos a remoção da mesma em um outro dataset
        # Para isso, copiamos o original para futura referência

        # Cópia do Dataset para alteração
        self.ds = self.data.copy()

        sns.countplot(data=self.ds, x='Race', hue='Status')
        plt.show()

        # Remoção da linha duplicada
        

        