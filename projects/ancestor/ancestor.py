class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, person):
    
    graph = {}

    for relationship in ancestors:
        parent = relationship[0]
        child = relationship[1]
        if child in graph:
            graph[child].add(parent)
        else:
            graph[child] = set()
            graph[child].add(parent)
    if person not in graph:
        return -1
    else:
        def dft(graph, starting_vertex):
            s = Stack()
            s.push([starting_vertex])
            visited = set()
            paths = {}
            maxLength = 0
            while s.size() > 0:
                path = s.pop()
                node = path[-1]
                if node not in visited and node in graph:
                    visited.add(node)
                    for parent in graph[node]:
                        new_path = path[:]
                        new_path.append(parent)
                        s.push(new_path)
                elif node not in graph:
                    length = len(path)
                    if length > maxLength:
                        maxLength = length
                    if length not in paths:
                        paths[length] = [path]
                    else:
                        paths[length].append(path)
            if len(paths[maxLength]) == 1:
                return paths[maxLength][0][-1]
            else:
                y = []
                for x in paths[maxLength]:
                    y.append(x[-1])
                return min(y)
        ancestor = dft(graph, person)
        
        return ancestor