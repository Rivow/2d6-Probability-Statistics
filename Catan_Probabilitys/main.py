from unittest import main
import Catan_Probabilitys

if __name__ == '__main__':
    game_end = False
    roll_list = []
    total_rolls = 0

    #Game Loop while game is still being played ends once Y or y given to comandline

    while game_end == False:
        roll = input('Dice Roll: ')
        number = Catan_Probabilitys.prove_if_int(roll)
        if number is True:
            range = Catan_Probabilitys.prove_range(int(roll))
        
        if range is True and number is True:
            game_rolled_list = Catan_Probabilitys.create_roll_list(int(roll), roll_list)
            total_rolls = Catan_Probabilitys.total_roll(total_rolls)
            end_question = input('Has the game ended? (Y/y) ')
            game_end = Catan_Probabilitys.game_ended(end_question)
            


    #The Probabiltys will be compared and plotted in for comparison
    probs = Catan_Probabilitys.create_average_probability_dic()



    roll_list = Catan_Probabilitys.rolled_dic(game_rolled_list)
    amount_rolls = Catan_Probabilitys.expected_amount_rolls(probs, total_rolls)
    for rolls in roll_list:
        if rolls < 10:
            print(f'{rolls}  Expected: {amount_rolls[rolls]}   Actual In Game: {roll_list[rolls]}  ')
        else:
            print(f'{rolls} Expected: {amount_rolls[rolls]}   Actual In Game: {roll_list[rolls]}  ')
    print(f'Total Rolls: {total_rolls}')

    main(module='Test_Module', exit=False)
