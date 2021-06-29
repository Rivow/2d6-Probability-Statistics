import unittest
import DiceProbabilityStatistics


class TestModule(unittest.TestCase):

#################################
#### All Probability Tests ######
#################################

    def test_create_avarege_probability_dic(self):
         actual = DiceProbabilityStatistics.create_average_probability_dic()
         expected = {2: 0.0278, 3: 0.0556, 4: 0.0833, 5: 0.1111, 6: 0.1389, 7: 0.1667, 8: 0.1389, 9: 0.1111, 10: 0.0833, 11: 0.0556, 12: 0.0278}
         self.assertDictEqual(actual, expected, 'Expected Dictionaries to be equal ')

    def test_calculate_game_prob(self):
        actual = DiceProbabilityStatistics.calculate_game_prob({2: 0, 3: 1, 4: 1, 5: 1, 6: 0, 7: 4, 8: 2, 9: 2, 10: 2, 11: 1, 12: 1}, 15)
        expected = {2: 0.6551, 3: 0.3744, 4: 0.3698, 5: 0.3204, 6: 0.1061, 7: 0.1418, 8: 0.2899, 9: 0.2804, 10: 0.2352, 11: 0.3744, 12: 0.2810}
        self.assertDictEqual(actual, expected, 'Expected both Dics to be Equal')

    def test_expected_amount_rolls(self):
        actual = DiceProbabilityStatistics.expected_amount_rolls({2: 0.0278, 3: 0.0556, 4: 0.0833, 5: 0.1111, 6: 0.1389, 7: 0.1667, 8: 0.1389, 9: 0.1111, 10: 0.0833, 11: 0.0556, 12: 0.0278}, 135)
        expected =  {2: 3.75, 3: 7.51 , 4: 11.25, 5: 15.0, 6: 18.75, 7: 22.5, 8: 18.75, 9: 15.0, 10: 11.25, 11: 7.51, 12: 3.75}
        self.assertDictEqual(actual, expected, 'Expected Dictionaries to be equal ')

    def test_at_least_prob(self):
        pass

#################################
#### All Math Tests ############
#################################
    
    def test_binomial(self):
        actual = DiceProbabilityStatistics.binomial(15, 7)
        expected = 6435
        self.assertEqual(actual, expected, 'Expected to be 6435 Combinations')

    

    
if __name__ == '__main__':
    unittest.main()
