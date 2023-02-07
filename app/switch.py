from app.data_base import ShowDatabase
from app.bagged_decision_tree import BaggedDecisionTree

class Switch:

    def __init__(self) -> None:
        
        self.running = True

        while self.running:
            print(f'\n------------- Algoritmos -------------')

            print('1 - Bagged Decision Tree..............')
            print('2 - Show Datas')
            print('0 - Exit Program......................')

            print(f'--------------------------------------\n')

            self.choice = int(input('Escolha uma opção: '))


            match self.choice:
                case 0:
                    self.running = False
                    print('Saindo...')
                case 1:
                    BaggedDecisionTree()
                case 2:
                    ShowDatabase()
            
            input("Press Enter to continue...")
