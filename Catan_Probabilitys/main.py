from unittest import main
import Catan_Probabilitys

if __name__ == '__main__':
    game_end = False
    roll_list = []
    total_rolls = 0
    while game_end == False:
        roll = input('Dice Roll: ')
        number = Catan_Probabilitys.prove_if_int(roll)
        range = Catan_Probabilitys.prove_range(roll)
        
        if number is True and range is True:
           
            new_list = Catan_Probabilitys.create_roll_list(roll, roll_list)
            Catan_Probabilitys.total_roll(total_rolls)
            end_question = input('Has the game ended? (Y/y) ')
            game_end = Catan_Probabilitys.game_ended(end_question)




    roll_list = Catan_Probabilitys.rolled_dic(roll_list)
    print(roll_list)

    main(module='Test_Module', exit=False)
