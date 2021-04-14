import unittest
import Catan_Probabilitys


class TestModule(unittest.TestCase):

    def test_prove_int_true(self):
        actual = Catan_Probabilitys.prove_if_int(2)
        self.assertTrue(actual, 'Expected True since test input was an integer')

    def test_prove_int_false(self):
        actual = Catan_Probabilitys.prove_if_int('e')
        self.assertFalse(actual, 'Expected False since test input is not an integer')

    def test_all_numbers_dic(self):
        actual = Catan_Probabilitys.create_dic()
        expected = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
        self.assertDictEqual(actual, expected, 'Expected Dictionaries to be equal ')

    def test_dic_numbers_rolled(self):
        roll = [7, 9, 12, 8, 10, 9, 11]
        actual = Catan_Probabilitys.rolled_dic(roll)
        expected = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1, 9: 2, 10: 1, 11: 1, 12: 1}
        self.assertDictEqual(actual, expected, 'Expected Dictionaries to be equal')


if __name__ == '__main__':
    unittest.main()
