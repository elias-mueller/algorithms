from collections import defaultdict

frontier = set()
visited = []
neighbours_by_node = defaultdict(set)


def _extract_neighbors(edges_list):
	assert len(edges_list) % 2 == 0
	edges = [(edges_list[i], edges_list[i+1]) for i in range(0, len(edges_list) - 1, 2)]
	for e in edges:
		neighbours_by_node[e[0]].add(e[1])


def bfs(edges_list):
	_extract_neighbors(edges_list)
	frontier.add(edges_list[0])
	while frontier:
		n = frontier.pop()
		visited.append(n)
		for n in neighbours_by_node[n]:
			if n in visited:
				continue
			frontier.add(n)
	return visited
