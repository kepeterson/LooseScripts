def visit(node, theGraph):
        neighbors = theGraph[node]
        allNodes = neighbors[:]
        print neighbors
        for neighbor in neighbors:
            allNodes.append(visit(neighbor, theGraph))
            print allNodes

        return neighbors


def visit2(node, fromNode, theGraph, visited):
    neighbors = theGraph[node]
    if fromNode in neighbors: neighbors.remove[fromNode]
    visited.append(node)
    for neighbor in neighbors:
        if neighbor not in visited:
            return visit2(neighbor, node, theGraph, visited)

    visited.append(node)
    return visited


def depthfirst(node, graph, visited):
    neighbors = graph[node]
    visited.append(node)
    for ne in neighbors:
        if ne not in visited:
            return depthfirst(ne, graph, visited)

    return visited