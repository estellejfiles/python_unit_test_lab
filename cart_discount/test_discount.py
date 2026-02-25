import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    #1
    def test_list_of_three_prices(self):
        # arrange - setting up test data
        prices = [10, 4, 20]
        expected_discount = 4
        # action - do the thing we want to test
        function_returned_discount = discount(prices)
        # assert - check that expected result matches actual result
        self.assertEqual(expected_discount, function_returned_discount)

    #2
    # at least one complete test for a happy path (expected scenario)
    def test_list_of_two_prices(self):
        # arrange
        prices = [10, 4]
        expected_discount = 0
        # act
        function_returned_discount = discount(prices)
        # assert
        self.assertEqual(expected_discount, function_returned_discount)

    #3
    # at least one complete test for an unhappy path (unexpected scenario)
    def test_integer_not_list(self):
        # arrange
        prices = 10
        # act and assert - we expect this to raise an error
        with self.assertRaises(TypeError):
            discount(prices)

    #4
    # other tests - write the test method header
    def test_discount_empty_list(self):
        # reminder to finish this test
        self.fail('finish this test')
    
    #5
    def test_string_not_list(self):
        self.fail('finish this test')
    
    #6
    def test_list_of_differing_types_of_items(self):
        self.fail('finish this test')

    #7
    def test_different_item_types(self):
        self.fail('finish this test')

    #8
    def test_none_input(self):
        self.fail('finish this test')

    #9
    def test_list_of_one_price(self):
        self.fail('finish this test')

    #10
    def test_list_of_negative_prices(self):
        self.fail('finish this test')

    #11
    def test_list_of_zero_prices(self):
        self.fail('finish this test')

    #12
    def test_list_of_float_prices(self):
        self.fail('finish this test')

    #13
    def test_list_of_mixed_int_and_float_prices(self):
        self.fail('finish this test')

    #14
    def test_all_items_same_price(self):
        self.fail('finish this test')

    #15
    # Ex: [10000000000 ** 1000000000000, 4, 20]
    def test_list_of_large_numbers(self):
        self.fail('finish this test')

    #16
    def test_list_with_zero_divisor(self):
        self.fail('finish this test')

    #17
    def test_list_of_strings(self):
        self.fail('finish this test')

    


if __name__ == '__main__':
    unittest.main()