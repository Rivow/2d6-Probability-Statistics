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


def calculate_game_prob(probability_dic):
    avarage_probability = create_averahe_probability_dic() 
    for number in probability_dic:
        



#################################
######## Math Functions #########
#################################

def binomial(total, expected):
    binomial_var = math.factorial(total)/(math.factorial(expected) * math.factorial(total - expected))
    return binomial_var


