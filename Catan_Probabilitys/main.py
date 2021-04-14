from unittest import main
import Catan_Probabilitys

if __name__ == '__main__':
    roll = input('Dice Roll: ')
    temp = Catan_Probabilitys.prove_if_int(roll)

    roll_list = Catan_Probabilitys.rolled_dic([2, 4, 6, 7, 7, 7, 9, 12, 10, 12])
    print(roll_list)

    main(module='Test_Module', exit=False)
