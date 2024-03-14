#from Problem import *
from SearchingAlgorithms import *

class Test(Problem):
	def actions(self, state):
		possible_actions = [];

		if state == 'A':
			possible_actions = ['A->B','A->C','A->I','A->L','A->N']
		elif state == 'B':
			possible_actions = ['B->A','B->E']
		elif state == 'C':
			possible_actions = ['C->A','C->D']
		elif state == 'D':
			possible_actions = ['D->C','D->F']
		elif state == 'E':
			possible_actions = ['E->B','E->P']
		elif state == 'F':
			possible_actions = ['F->D','F->M']
		elif state == 'G':
			possible_actions = ['G->N','G->P']
		elif state == 'H':
			possible_actions = ['H->I']
		elif state == 'I':
			possible_actions = ['I->A','I->H']
		elif state == 'L':
			possible_actions = ['L->A','L->M']
		elif state == 'M':
			possible_actions = ['M->F''M->L',]
		elif state == 'N':
			possible_actions = ['N->A','N->G']
		elif state == 'P':
			possible_actions = ['P->E','P->G']
		else:
			possible_actions = []
		
		return possible_actions;

	def step_cost(self, action, stateA= None, stateB = None):
		tmp = (action,f"{action[-1]}->{action[0]}") # x grafo non diretto

		if  'A->L' in tmp or 'I->H' in tmp or 'A->B' in tmp or  'B->E' in tmp or 'D->F' in tmp or 'M->F' in tmp or 'M->L' in tmp:
			return 2;
		elif 'A->I'in tmp:
			return 1;
		elif 'A->N' in tmp or 'G->P' in tmp or 'P->E' in tmp:
			return 5;
		elif 'C->D' in tmp or 'A->C' in tmp:
			return 10;
		else:
			return 4;

	def value(self,node):
		if node.state == 'C' or node.state == 'F' or node.state == 'G' or node.state == 'E':
			return 1;
		elif node.state == 'A' or node.state == 'M' or node.state == 'N' or node.state == 'B':
			return 2;	
		elif node.state == 'L' or node.state == 'I':
			return 3;
		elif node.state == 'H':
			return 4;
		else:
			return 0;

	def result(self, state, action):
	    # Dato lo stato state e l'azione action, restituisce il nuovo stato
	    new_state = '' # inizializza il nuovo stato
	    # in questo caso il nuovo stato e' semplicemente l'ultimo carattere
	    # della stringa che definisce l'azione
	    new_state = action[-1:];
	    
	    return new_state;



def h(node):
	if node.state == 'C' or node.state == 'F' or node.state == 'G' or node.state == 'E':
		return 1;
	elif node.state == 'A' or node.state == 'M' or node.state == 'N' or node.state == 'B':
		return 2;	
	elif node.state == 'L' or node.state == 'I':
		return 3;
	elif node.state == 'H':
		return 4;
	else:
		return 0;

def hill_climbing(problem):
	""" Ricerca locale - Hill-climbing."""
	current = Node(problem.initial_state)
	while True:
		print(f"Discesa rapida esplora {current.state} con goal={problem.goal_state}")

		neighbors =  [current.child_node(problem, action) for action in problem.actions(current.state)]
		# se current non ha successori esci e restituisci current
		if not neighbors:
			break
		
		# scegli il vicino con valore piu' alto
		neighbor = (sorted(neighbors,key = lambda x:problem.value(x), reverse = False))[0] #reverse = True => ascesa
		if problem.value(neighbor) >= problem.value(current):
			break
		else:
			current = neighbor
	return current

def a_search(problem):
	"""Ricerca-grafo UC"""
	explored = [] # insieme (implementato come una lista) degli stati gia' visitati
	node = Node(problem.initial_state) # il costo del cammino e' inizializzato nel costruttore del nodo
	# la frontiera e' una coda coda con priorita'
	frontier = PriorityQueue(f = lambda x:x.path_cost+h(x)) #lambda serve a definire una funzione anonima a runtime
	frontier.insert(node)
	while not frontier.isempty():
		# seleziona il nodo per l'espansione
		node = frontier.pop() # estrae il nodo con costo minore
		# controlla se lo stato del nodo e' uno stato obiettivo
		if problem.goal_test(node.state):
			return node.solution(explored_set = explored)
		else:
			# se non lo e' inserisci lo stato nell'insieme degli esplorati
			explored.append(node.state)
			print('A esploro lo stato '+node.state+' con costo {}'.format(node.path_cost)+f' con goal={problem.goal_state}')
		for action in problem.actions(node.state):
			child_node = node.child_node(problem, action)
			# controlla se lo stato del nodo figlio non e' nell'insieme dei nodi esplorati
			# e non e' nella frontiera
			if (child_node.state not in explored) and (not frontier.contains_state(child_node.state)):
				frontier.insert(child_node)
			# se lo stato del nodo figlio e' gia' nella frontiera, ma con un costo piu' alto
			# allora sostituisci il nodo nella frontiera con il nodo figlio
			elif frontier.contains_state(child_node.state) and (frontier.get_node(frontier.index_state(child_node.state)).path_cost >
																child_node.path_cost):
				frontier.remove(frontier.index_state(child_node.state))
				frontier.insert(child_node)

	return None # in questo caso ritorna con fallimento

def uniform_cost_search(problem):
	"""Ricerca-grafo UC"""
	explored = [] # insieme (implementato come una lista) degli stati gia' visitati
	node = Node(problem.initial_state) # il costo del cammino e' inizializzato nel costruttore del nodo
	# la frontiera e' una coda coda con priorita'
	frontier = PriorityQueue(f = lambda x:x.path_cost) #lambda serve a definire una funzione anonima a runtime
	frontier.insert(node)
	while not frontier.isempty():
		# seleziona il nodo per l'espansione
		node = frontier.pop() # estrae il nodo con costo minore
		# controlla se lo stato del nodo e' uno stato obiettivo
		if problem.goal_test(node.state):
			return node.solution(explored_set = explored)
		else:
			# se non lo e' inserisci lo stato nell'insieme degli esplorati
			explored.append(node.state)
			print('UC esploro lo stato '+node.state+' con costo {}'.format(node.path_cost)+f' con goal={problem.goal_state}')
		for action in problem.actions(node.state):
			child_node = node.child_node(problem, action)
			# controlla se lo stato del nodo figlio non e' nell'insieme dei nodi esplorati
			# e non e' nella frontiera
			if (child_node.state not in explored) and (not frontier.contains_state(child_node.state)):
				frontier.insert(child_node)
			# se lo stato del nodo figlio e' gia' nella frontiera, ma con un costo piu' alto
			# allora sostituisci il nodo nella frontiera con il nodo figlio
			elif frontier.contains_state(child_node.state) and (frontier.get_node(frontier.index_state(child_node.state)).path_cost >
																child_node.path_cost):
				frontier.remove(frontier.index_state(child_node.state))
				frontier.insert(child_node)

	return None # in questo caso ritorna con fallimento

def depth_first_search_graph(problem):
	"""Ricerca-grafo in profondita' """
	explored = [] # insieme (implementato come una lista) degli stati gia' visitati
	node = Node(problem.initial_state) # il costo del cammino e' inizializzato nel costruttore del nodo 
	# controlla se lo stato iniziale e' uno stato obiettivo
	if problem.goal_test(node.state):
		return node.solution()
	frontier = LIFOQueue() #la frontiera e' una coda LIFO
	frontier.insert(node)
	while not frontier.isempty():
		node = frontier.pop() #estrae il nodo dalla frontiera
		# controlla se lo stato del nodo e' uno stato obiettivo
		if problem.goal_test(node.state):
			return node.solution(explored_set = explored)
		else:
			# se lo stato non e' uno stato obiettivo aggiungilo all'insieme degli esplorati
			explored.append(node.state)
		# espandi la frontiera
		print(f"DF con goal={problem.goal_state} esploro nodo {node.state}")
		for action in problem.actions(node.state):
			child_node = node.child_node(problem,action)
			if (child_node.state not in explored) and (not frontier.contains(child_node.state)):
				frontier.insert(child_node)
	return None # in questo caso ritorna con fallimento



print(depth_first_search_graph(Test('A','D')))
print(depth_first_search_graph(Test('A','P')))
print(uniform_cost_search(Test('A','D')))
print(uniform_cost_search(Test('A','P')))
print(a_search(Test('A','D')))
print(a_search(Test('A','P')))
print(hill_climbing(Test('A','D')))
print(hill_climbing(Test('A','P')))