processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_node = None
    for node in costs:
        cost = costs[node]
        if node not in processed and cost < lowest_cost:
            lowest_cost = cost
            lowest_node = node
    return lowest_node

def algorithm(costs, graph, parents):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for i in neighbors.keys():
            new_cost = cost + neighbors[i]
            if costs[i] > new_cost:
                costs[i] = new_cost
                parents[i] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)