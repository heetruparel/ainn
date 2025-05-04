import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.costs = {}
        self.heuristics = {}

    def add_edge(self, from_node, to_node, cost):
        self.edges[from_node].append(to_node)
        self.costs[(from_node, to_node)] = cost

    def add_heuristic(self, node, h_value):
        self.heuristics[node] = h_value

def astar(graph, start, goal):
    frontier = [(graph.heuristics[start], start)]  # Priority queue with f_cost, node
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for neighbor in graph.edges[current]:
            new_cost = cost_so_far[current] + graph.costs[(current, neighbor)]

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                f_cost = new_cost + graph.heuristics[neighbor]  # f_cost = g_cost + h_cost
                heapq.heappush(frontier, (f_cost, neighbor))  # Push to frontier
                came_from[neighbor] = current

    # Reconstruct the path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = came_from[node]
    path.reverse()

    return path, cost_so_far[goal]

def main():
    # Create graph
    g = Graph()
    g.add_edge('S', 'A', 1)
    g.add_edge('S', 'G', 10)
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 3)
    g.add_edge('C', 'G', 4)
    g.add_edge('D', 'G', 4)

    # Add heuristic values
    g.add_heuristic('S', 5)
    g.add_heuristic('A', 3)
    g.add_heuristic('B', 4)
    g.add_heuristic('C', 2)
    g.add_heuristic('D', 6)
    g.add_heuristic('G', 0)

    # Run A* algorithm
    start_node = 'S'
    goal_node = 'G'
    path, total_cost = astar(g, start_node, goal_node)

    # Output the result
    print("Path found:", " -> ".join(path))
    print("Total cost:", total_cost)

if __name__ == "__main__":
    main()
