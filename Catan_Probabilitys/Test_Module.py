import unittest
import Catan_Probabilitys


class TestModule(unittest.TestCase):

#################################
#######All Game Tests ###########
#################################

    def test_prove_int_true(self):
        actual = Catan_Probabilitys.prove_if_int(2)
        self.assertTrue(actual, 'Expected True since test input was an integer')

    def test_prove_int_false(self):
        actual = Catan_Probabilitys.prove_if_int('e')
        self.assertFalse(actual, 'Expected False since test input is not an integer')


    def test_prove_range_in(self):
        actual = Catan_Probabilitys.prove_range(12)
        self.assertTrue(actual, 'Expected 5 to be in Dice Roll Range')


    def test_prove_range_out(self):
        actual = Catan_Probabilitys.prove_range(1)
        self.assertFalse(actual, 'Expected to Return False because 1 is not in Roll Range')


    def test_all_numbers_dic(self):
        actual = Catan_Probabilitys.create_dic()
        expected = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
        self.assertDictEqual(actual, expected, 'Expected Dictionaries to be equal ')

    def test_dic_numbers_rolled(self):
        roll = [7, 9, 12, 8, 10, 9, 11]
        actual = Catan_Probabilitys.rolled_dic(roll)
        expected = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1, 9: 2, 10: 1, 11: 1, 12: 1}
        self.assertDictEqual(actual, expected, 'Expected Dictionaries to be equal')

    def test_total_rolls(self):
        actual = Catan_Probabilitys.total_roll(6)
        expected = 7 
        self.assertEqual(actual, expected, 'Expected Total Rolls to be 7')

    def test_create_roll_list(self):
        roll_list = []
        for test_var in range(2,10):
            actual = Catan_Probabilitys.create_roll_list(test_var, roll_list)
        expected = [2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(actual, expected, 'Roll List Expected to have the values form 2 to 9')


    def test_if_game_ended_lower(self):
        actual = Catan_Probabilitys.game_ended
        self.assertTrue(actual, 'Expected to return True')


    def test_if_game_ended_upper(self):
        actual = Catan_Probabilitys.game_ended
        self.assertTrue(actual, 'Expected to return True')

#################################
#### All Probability Tests ######
#################################

    def test_create_avarege_probability_dic(self):
         actual = Catan_Probabilitys.create_average_probability_dic()
         expected = {2: 0.0278, 3: 0.0556, 4: 0.0833, 5: 0.1111, 6: 0.1389, 7: 0.1667, 8: 0.1389, 9: 0.1111, 10: 0.0833, 11: 0.0556, 12: 0.0278}
         self.assertDictEqual(actual, expected, 'Expected Dictionaries to be equal ')

    def test_calculate_game_prob(self):
        actual = Catan_Probabilitys.calculate_game_prob({2: 0, 3: 1, 4: 1, 5: 1, 6: 0, 7: 4, 8: 2, 9: 2, 10: 2, 11: 1, 12: 1}, 15)
        expected = {2: 0.6551, 3: 0.3744, 4: 0.3698, 5: 0.3204, 6: 0.1061, 7: 0.1418, 8: 0.2899, 9: 0.2804, 10: 0.2352, 11: 0.3744, 12: 0.2810}
        self.assertDictEqual(actual, expected, 'Expected both Dics to be Equal')

    def test_expected_amount_rolls(self):
        actual = Catan_Probabilitys.expected_amount_rolls({2: 0.0278, 3: 0.0556, 4: 0.0833, 5: 0.1111, 6: 0.1389, 7: 0.1667, 8: 0.1389, 9: 0.1111, 10: 0.0833, 11: 0.0556, 12: 0.0278}, 135)
        expected =  {2: 3.75, 3: 7.51 , 4: 11.25, 5: 15.0, 6: 18.75, 7: 22.5, 8: 18.75, 9: 15.0, 10: 11.25, 11: 7.51, 12: 3.75}
        self.assertDictEqual(actual, expected, 'Expected Dictionaries to be equal ')

    def test_at_least_prob(self):
        pass

#################################
#### All Math Tests ############
#################################
    
    def test_binomial(self):
        actual = Catan_Probabilitys.binomial(15, 7)
        expected = 6435
        self.assertEqual(actual, expected, 'Expected to be 6435 Combinations')

    

    
if __name__ == '__main__':
    unittest.main()
