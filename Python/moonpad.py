import math

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, l = map(int, raw_input().split())
graph = {}
for i in xrange(N):
    graph[i] = set()

for i in xrange(l):
    a, b = map(int, raw_input().split())
    if a in graph:
        graph.get(a).add(b)
        
    if b in graph:
        graph.get(b).add(a)

print graph


def depthfirst(node, ingraph, visited):
    neighbors = ingraph[node]
    visited.append(node)
    for ne in neighbors:
        if ne not in visited:
            visited+depthfirst(ne, ingraph, visited)

    return visited

components = []
while graph:
    firstNode = min(graph.keys())
    print firstNode
    results = depthfirst(firstNode, graph, [])
    print "results: "+str(results)
    components.append(results)

    for re in results:
        del graph[re]

#the problem is unconnected nodes. Need to build out the
#set of nodes in the graph entirely
#when they are searched they need to return length 1
print components

counts = map(lambda x: len(x), components)
if len(counts) == 1:
    print 0
else:
    #results = reduce(lambda x, y: x * y, counts, 1) * math.factorial(len(counts))/(2 * math.factorial(len(counts) - 2))
# Compute the final result using the inputs from above
    head, tail = counts[0], counts[1:]
    results = 0
    while len(tail) > 0:
        results += sum(map(lambda x: head * x, tail))
        head, tail = tail[0], tail[1:]

    print results

