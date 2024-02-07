# (30/1/24)

![[1-IIA-24-introduzione-V1.0.pdf]]

![[2-IIA-2024-agents.pdf]]


![[3-IIA-2024-problem_solving.pdf]]

```python
"""Ricerca-grafo in ampiezza"""

def BF(problem): #CODA -> PUSH E UNSHIFT -> FIFO

    # explored = []

    # node = Node(problem.initial_state)

    # if problem.goal_test(node.state):

    #     return node.solution(explored_set = explored)

    # frontier = FIFOQueue()

    # frontier.insert(node)

    # while not frontier.isempty():

    #     node = frontier.pop()

    #     explored.append(node.state)

    #     for action in problem.actions(node.state):

    #         child_node = node.child_node(problem,action)

    #         if (child_node.state not in explored) and (not frontier.contains_state(child_node.state)):

    #             if problem.goal_test(child_node.state):

    #                 return child_node.solution(explored_set = explored)

    #             frontier.insert(child_node)

    return None
```

```python
"""Ricerca in profondita' ricorsiva """

def DF_ricorsiva(problem,node): #STACK -> PUSH E POP -> LIFO

    # if problem.goal_test(node.state):

    #     return node.solution()

    # for action in problem.actions(node.state):

    #     child_node = node.child_node(problem, action)

    #     result = DF_ricorsiva(problem, child_node)

    #     if result is not None:

    #         return result

    return None
```

```python
"""Ricerca-grafo UC"""

def UC(problem):

    # explored = []

    # node = Node(problem.initial_state)

    # frontier = PriorityQueue(f = lambda x:x.path_cost)

    # frontier.insert(node)

    # while not frontier.isempty():

    #     node = frontier.pop()

    #     if problem.goal_test(node.state):

    #         return node.solution(explored_set = explored)

    #     else:

    #         explored.append(node.state)

    #     for action in problem.actions(node.state):

    #         child_node = node.child_node(problem, action)

    #         if (child_node.state not in explored) and (not frontier.contains_state(child_node.state)):

    #             frontier.insert(child_node)

    #         elif frontier.contains_state(child_node.state) and (frontier.get_node(frontier.index_state(child_node.state)).path_cost > child_node.path_cost):

    #             frontier.remove(frontier.index_state(child_node.state))

    #             frontier.insert(child_node)

  

    return None
```

