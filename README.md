# Shortest-Path--A-Star-Algorithm
In  this  project, toy  water  pitcher  problem is used  to  expand  on understanding  of  the  “search” problem.  The learning objectives are:  (i) Search problem  (ii) Dynamically creating a graph, when there are no nodes or edges in sight.  (iii) A* algorithm, heuristic, and lower bound

The solution Python code `a_star_water_pitchers.py` implements the `A* algorithm` to solve a water pouring puzzle. The puzzle involves two or more jugs of different capacities and a target quantity of water to be measured using these jugs. The algorithm finds the minimum number of steps required to measure the target quantity of water, or returns -1 if it is not possible.

The `WaterPuzzle` class reads input from a file, initializes the jug capacities and target quantity, defines the initial state, calculates the `heuristic` function, generates `potential states` and performs the `A* search`. The `read_input_file` function reads the input file and returns a tuple of jug capacities and target quantity. The `initial_state` function returns a tuple representing the state where all jugs are empty. The `heuristic` function calculates the estimated distance from the current state to the goal state, which is the sum of actual and next distance to the target quantity. The potential_states function generates the possible next states that can be reached from the current state. The `a_star_search` function performs the A* search and returns the minimum number of steps required to measure the target quantity of water, or returns -1 if it is not possible.

In the main program, the WaterPuzzle object is created using the input file `input.txt`, and the a_star_search function is called on the object with the jug capacities and target quantity as input parameters. The minimum number of steps required to measure the target quantity is then printed to the console.

Finally, a unit test module written in Python `test_a_star_water_pitchers.py` using the `unittest` library is used to check the results. It tests the WaterPuzzle class from the a_star_water_pitchers module. The class is instantiated with an input file `input.txt`, which is assumed to contain valid input for the water puzzle problem.

The test_cases class contains five test cases, each testing the a_star_search method of the `WaterPuzzle class` with different input parameters. For each test case, the expected outcome is compared to the actual output of the a_star_search method using the `self.assertEqual()` method provided by the unittest library.

The purpose of this unit test is to verify that the `a_star_search` method of the `WaterPuzzle class` returns the expected output for a range of different inputs. If all test cases pass, it indicates that the implementation of the WaterPuzzle class is correct and that the a_star_search method is working as expected.
