import heapq
import sys

class WaterPuzzle:
    def __init__(self, file_path):
        self.jug_capacities, self.target_quantity = self.read_input_file(file_path)

    def read_input_file(self, file_path):
        with open(file_path) as f:
            my_tuple = tuple(map(int, f.readline().strip().split(',')))
            target_quantity = int(f.readline())
            jug_capacities = (sys.maxsize,) + my_tuple
        return jug_capacities, target_quantity

    def initial_state(self):
        return (0,) * len(self.jug_capacities)

    def heuristic(self, state):
        if state[0] == self.target_quantity:
            return 0

        remaining_quantity=self.target_quantity - state[0]
            
        # Check if any jugs contain the target quantity and return inverse
        for jug in range(1, len(self.jug_capacities)):
            if state[0] + state[jug] == self.target_quantity and state[jug] > 0:
                return 1 / self.target_quantity
    
            
        # Check if any jugs can be filled to reach the target quantity
        for jug in range(len(self.jug_capacities)):
            if remaining_quantity== max(state[1:]) + self.jug_capacities[jug]:
                return (((remaining_quantity + self.jug_capacities[jug])) / 2) / self.target_quantity
            
        # Return the sum of actual and next distance to target quantity
        return (remaining_quantity + abs(remaining_quantity - max(state[1:]))) / self.target_quantity

    def potential_states(self, state):
    # Initialize an empty list to hold the next possible states
        potential_states = []
        # Iterate through the state list
        for i, amt in enumerate(state):
            # Skip the first element of the list (target quantity)
            if i == 0:
                continue
            # Create a new state with the i-th jug emptied
            new_state_empty = list(state)
            new_state_empty[i] = 0
            potential_states.append(new_state_empty)

            # Create a new state with the i-th jug filled to capacity
            new_state = list(state)
            if amt == 0:
                new_state[i] += self.jug_capacities[i]
                potential_states.append(new_state)
            else:
                # Iterate through the other jugs
                for j, _ in enumerate(state):
                    # Skip the same jug
                    if i == j:
                        continue
                    # Fill the other jug from i-th jug if possible
                    if amt >= self.jug_capacities[j] - state[j] and self.jug_capacities[j] - state[j] >= 0:
                        new_state = list(state)
                        new_state[i] = (amt - (self.jug_capacities[j] - state[j]))
                        new_state[j] = new_state[j] + (self.jug_capacities[j] - state[j])
                        potential_states.append(new_state)
                    # Fill the other jug from i-th jug if it doesn't overflow
                    elif amt < self.jug_capacities[j] - state[j]:
                        new_state = list(state)
                        new_state[i] = 0
                        new_state[j] = new_state[j] + amt
                        potential_states.append(new_state)

        # Return the list of next possible states
        return potential_states

    def a_star_search(self,jug_capacities, target_quantity):
        initial_state = self.initial_state()
        fringe = [(self.heuristic(initial_state), 0, initial_state)]
        already_explored = set()
        while fringe:
            h, g, current_state = heapq.heappop(fringe)

            if current_state[0] > target_quantity:
                continue

            if str(current_state) in already_explored:
                continue

            if current_state[0] == target_quantity:
                return g

            while fringe:
                h_, g_, _ = heapq.heappop(fringe)

            already_explored.add(str(current_state))

            for next in self.potential_states(current_state):
                next_cost = g + 1
                total_cost = next_cost + self.heuristic(next)
                heapq.heappush(fringe, (total_cost, next_cost, next))

            if current_state[0] > target_quantity + 2 * max(jug_capacities[1:]):
                return -1
        return -1

if __name__ == '__main__':
    pitch = WaterPuzzle('input.txt')
    print(pitch.a_star_search(pitch.jug_capacities, pitch.target_quantity))