import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class ShowDatabase:

    def __init__(self) -> None:
        self.df = pd.read_csv('app/data/Breast_Cancer.csv')

        #self.df = self.df.head()

        #self.showHead()
        self.showColumns()
        #self.showNulls()
        #self.showGraphBarra()
        #self.showGraphArrai()
        #self.showGraphDispersso()


    def showHead(self) -> None:
        print(f'Database: \n{self.df.head()}')
    
    def showColumns(self) -> None:
        print(f'Columns: \n{self.df.columns}')
    
    def showNulls(self) -> None:
        print(f'Nulss: \n{self.df.isnull().sum()}')
    
    def showGraphBarra(self):
        sns.countplot(x=self.df["Tumor Size"])

        plt.xticks(rotation = 95)
        plt.show()
    
    def showGraphArrai(self):
        sns.violinplot(x=self.df['Race'], y=self.df['Tumor Size'])
        
        plt.show()
    
    def showGraphDispersso(self):
        sns.lmplot(x='Age', y='Tumor Size', col='Race', data=self.df, markers='.', scatter_kws=dict(color='c'))

        plt.show()