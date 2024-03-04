from Problem import *
from Queue import *
from Node import *
from SearchingAlgorithms import *
        

class Problema(Problem):
	
	def __init__(self, initial_state, goal_state = None):
		self.initial_state = (0,initial_state);
		self.goal_state = goal_state;

	def actions(self,state):
		actions = [];
		if state[1] == 'S':
			actions = [(2,'B'),(1,'C'),(10,'D')]
		elif state[1] == 'D':
			actions = [(10,'S')]
		elif state[1] == 'C':
				actions = [(1,'S'),(15,'G')]
		elif state[1] == 'B':
			actions = [(2,'S'),(7,'E')]
		elif state[1] == 'E':
			actions = [(7,'B'),(1,'F'),(2,'G')]
		elif state[1] == 'G':
			actions = [(15,'C'),(2,'E'),(3,'F')]
		elif state[1] == 'F':
			actions = [(1,'E'),(3,'G')]

		return sorted(actions, key=lambda x: (x[0], x[1] if x[0] == min(action[0] for action in actions) else ord(x[1])));

	def result(self,state,action):
		return (state[0]+action[0],action[1])

	def goal_test(self,state):
		return state[1] == self.goal_state

	def __str__(self)




if __name__ == "__main__":
	print(breadth_first_search(Problema('S','G')))
	print(uniform_cost_search(Problema('S','G')))