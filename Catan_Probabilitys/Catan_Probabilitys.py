

def prove_if_int(integer):
    try:
        int(integer)
        return True

    except ValueError:
        print('Only Accepts Integers')
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



