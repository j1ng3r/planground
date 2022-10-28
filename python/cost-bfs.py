from queue import PriorityQueue
from math import log

baseprob = 0.9

graph = {
	'A' : [(baseprob ** 3, 'B'), (baseprob ** 4, 'C')],
	'B' : [(baseprob ** 6, 'D')],
	'C' : [(baseprob ** 2, 'D')],
	'D' : [(baseprob ** 1, 'E'), (baseprob ** 6, 'F')],
	'E' : [(baseprob ** 4, 'F')],
}

graph2 = {
	'X' : [(baseprob ** 1, 'Z'), (baseprob ** 13, 'A')],
	'Z' : [(baseprob ** 5, 'B')],
	'A' : [(baseprob ** 3, 'B'), (baseprob ** 4, 'C')],
	'C' : [(baseprob ** 2, 'D')],
	'B' : [(baseprob ** 6, 'D')],
	'D' : [(baseprob ** 3, 'E'), (baseprob ** 6, 'F')],
	'E' : [(baseprob ** 2, 'F')]
}

graph3 = {
	'X' : [(baseprob ** 1, 'Z'), (baseprob ** 2, 'A')],
	'Z' : [(baseprob ** 5, 'B')],
	'A' : [(baseprob ** 3, 'B'), (baseprob ** 4, 'C')],
	'C' : [(baseprob ** 2, 'D')],
	'B' : [(baseprob ** 6, 'D')],
	'D' : [(baseprob ** 3, 'E'), (baseprob ** 6, 'F')],
	'E' : [(baseprob ** 2, 'F')]
}

def prob_bfs(graph, root, destination):
	# Set of explored nodes
	explored = set(root)

	paths_pqueue = PriorityQueue() # Initialize a pqueue
	paths_pqueue.put((0, root))

	# loss = negative log probability
	while paths_pqueue:
		# total_prob=float+, path=node[]
		total_loss, path = paths_pqueue.get() # pqueue method
		node = path[-1]
		
		# check if we are at destination
		if node == destination:
			return path
		
		# loss in (0,1], neighbor is a node
		for loss, neighbor in graph[node]:
			if neighbor not in explored:
				paths_pqueue.put((total_loss + loss, path + neighbor))
		
		# done exploring paths, so append
		explored.add(node)

assert prob_bfs(graph, "A", "F") == "ACDEF"
assert prob_bfs(graph2, "X", "F") == "XZBDEF"
assert prob_bfs(graph3, "X", "F") == "XACDEF"
print("Let's GOOO!!")
