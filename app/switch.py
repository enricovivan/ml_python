
from .bagged_decidion_tree import BaggedDecisionTree

class Switch:

    def __init__(self) -> None:
        
        self.running = True

        while self.running:
            print(f'\n------------- Algoritmos -------------')

            print('1 - Bagged Decision Tree..............')
            print('0 - Exit Program......................')

            print(f'--------------------------------------\n')

            self.choice = int(input('Escolha uma opção: '))


            match self.choice:
                case 0:
                    self.running = False
                    print('Saindo...')
                case 1:
                    BaggedDecisionTree()
