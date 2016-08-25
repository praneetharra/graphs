graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

def graphsearch(graph, start, end, path):
    path = path + [start]
    if start == end:
        return path
    elif graph[start] == None:
        return None
    else:
        for node in graph[start]:
            newpath = graphsearch(graph, node, end, path)
            if newpath:
                return newpath
                
print(graphsearch(graph, 'A', 'D', []))
