from app.bagged_decidion_tree import BaggedDecisionTree

def main():
    
    running = True

    while running:
        print(f'\n------------- Algoritmos -------------')

        print('1 - Bagged Decision Tree..............')
        print('0 - Exit Program......................')

        print(f'--------------------------------------\n')

        choice = int(input('Escolha uma opção: '))


        match choice:
            case 0:
                running = False
            case 1:
                print('Bagged Decision Tree')

if __name__ == '__main__':
    main()