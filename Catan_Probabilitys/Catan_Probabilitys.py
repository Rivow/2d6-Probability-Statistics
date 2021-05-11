import math

#################################
#######All Game Functions########
#################################
def prove_if_int(integer):
    try:
        int(integer)
        return True

    except ValueError:
        print('Only Accepts Integers')
        return False


def prove_range(roll):
    if roll > 1 and roll < 13:
        return True
    else:
        print('The Roll must be between 2 and 12')
        return False


def create_dic():
    rolldic = {}
    for number in range(2, 13):
        rolldic.update({number: 0})

    return rolldic


def rolled_dic(roll_list):

    roll_dic = create_dic()

    for roll in roll_list:
        repeated_number = roll_list.count(roll)
        roll_dic[roll] = repeated_number

    return roll_dic


def create_roll_list(roll, roll_list):
    roll_list.append(roll)
    return roll_list
   

def total_roll(int):
    int += 1
    return int


def game_ended(end_question):
    if end_question == 'Y' or end_question == 'y':
        return True
    
    else:
        return False

#################################
#####Probability Functions#######
#################################

def create_average_probability_dic():
    avarage_probability_dic = {2: 0.0278, 3: 0.0556, 4: 0.0833, 5: 0.1111, 6: 0.1389, 7: 0.1667, 8: 0.1389, 9: 0.1111, 10: 0.0833, 11: 0.0556, 12: 0.0278}
    return avarage_probability_dic


def calculate_game_prob(roll_dic, total_rolls):
    game_prob_dic = {}
    avarage_probability = create_average_probability_dic() 
    for number in avarage_probability:
        binomial_roll = binomial(total_rolls, roll_dic[number])
        prob = binomial_roll * (avarage_probability[number]) ** roll_dic[number] * (1-avarage_probability[number]) ** (total_rolls - roll_dic[number])
        rounded = round(prob, 4)
        game_prob_dic[number] = rounded 
    return game_prob_dic 


def expected_amount_rolls(average_prob_dic, total_rolls):
    roll_amount_dic = {}
    for roll_prob in average_prob_dic:
        amount = average_prob_dic[roll_prob] * total_rolls
        rounded = round(amount, 2)
        roll_amount_dic[roll_prob] = rounded
    return roll_amount_dic


#################################
######## Math Functions #########
#################################

def binomial(total, no_rolls):
    binomial_var = math.factorial(total)/(math.factorial(no_rolls) * math.factorial(total - no_rolls))
    return binomial_var


