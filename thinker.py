import numpy

class Stack:
    def __init__(self, max):
        self.max = max
        self.top = -1
        self.stack = numpy.empty(max)

    def push(self, node):
        if self.top == self.max - 1:
            return

        self.top += 1
        self.stack[self.top] = node

    def pop(self):
        if self.empty():
            return
        
        self.top -= 1
        return self.stack[self.top + 1]
            
    def empty(self):
        if self.top + 1 == 0:
            return True
        else:
            return False
        
    def print(self):
        for i in range(self.top + 1):
            print(self.stack[i], end = " ")

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self, nodes):
        self.nodes = nodes # Representing root as well
        # Instantiates the number of arrays representing every edge between each node
        self.tree_map = [TreeNode(i) for i in range(nodes)]

    def add_edge(self, x, *y):
        # Assignment of both to each other makes them linked
        self.tree_map[x].children.append(y)

    def dfs_search(self, start, end):
        visited = ([False] * range(self.nodes))
        explored = Stack(self.nodes)

        considered = Stack(self.nodes)

        for i in range(len(self.tree_map)):
            if not visited[i]:
                if len(self.tree_map[i].children) == 0:
                    return explored
                else:
                    explored.push(self.tree_map[i])
                    visited[i] = True
                

    def bsf_search(self, start, end):
        pass

    def print(self):
        pass
    
brain = Tree(10)
brain.add_edge(1, 2, 3)
brain.add_edge(2, 4, 5)
brain.add_edge(3, 6, 7, 8, 9)
brain.add_edge(5, 10)

thoughts = Stack(5)
thoughts.push(5)
thoughts.push(5)
thoughts.push(5)
thoughts.push(5)
thoughts.push(5)
thoughts.push(5)
thoughts.pop()
thoughts.pop()
thoughts.pop()
thoughts.pop()
thoughts.pop()
thoughts.pop()

thoughts.print()