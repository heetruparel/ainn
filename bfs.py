graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(graph, start_node):
    visited = []
    queue = []
    result = []

    visited.append(start_node)
    queue.append(start_node)

    while queue:
        current = queue[0]
        result.append(current)
        queue = queue[1:]
        print(queue)

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

    print("Final result:")
    print(result)
    

bfs(graph, 'A')
