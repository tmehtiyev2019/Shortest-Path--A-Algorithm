import unittest
from a_star_water_pitchers import WaterPuzzle
import sys

test=WaterPuzzle("input.txt")
class test_cases(unittest.TestCase):

    def case_1(self):
        infinite_pitcher_capacity = sys.maxsize
        test.jug_capacities = (infinite_pitcher_capacity, 3)
        test.target_quantity = 10
        expected_outcome = -1
        self.assertEqual(test.a_star_search(test.jug_capacities, test.target_quantity), expected_outcome)


    def case_2(self):
        infinite_pitcher_capacity = sys.maxsize
        test.jug_capacities = (infinite_pitcher_capacity, 3, 6)
        test.target_quantity = 2
        expected_outcome = -1
        self.assertEqual(test.a_star_search(test.jug_capacities, test.target_quantity), expected_outcome)


    def case_3(self):
        infinite_pitcher_capacity = sys.maxsize
        test.jug_capacities = (infinite_pitcher_capacity, 1, 4, 10, 15, 22)
        test.target_quantity = 181
        expected_outcome = 20
        self.assertEqual(test.a_star_search(test.jug_capacities, test.target_quantity), expected_outcome)


    def case_4(self):
        infinite_pitcher_capacity = sys.maxsize
        test.jug_capacities = (infinite_pitcher_capacity, 2, 5, 6, 72)
        test.target_quantity = 143
        expected_outcome = 7
        self.assertEqual(test.a_star_search(test.jug_capacities, test.target_quantity), expected_outcome)

    def case_5(self):
        infinite_pitcher_capacity = sys.maxsize
        test.jug_capacities = (infinite_pitcher_capacity, 2, 3, 5, 19, 121, 852)
        test.target_quantity = 11443
        expected_outcome = 36
        self.assertEqual(test.a_star_search(test.jug_capacities, test.target_quantity), expected_outcome)
