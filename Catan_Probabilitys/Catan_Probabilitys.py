
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
