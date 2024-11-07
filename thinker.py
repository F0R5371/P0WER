import numpy

class Stack:
    def __init__(self, max):
        self.max = max
        self.top = -1
        self.stack = numpy.empty(max)

    def push(self, value):
        if self.top == self.max - 1:
            return

        self.top += 1
        self.stack[self.top] = value

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
        self.parent = None

class Tree:
    def __init__(self, nodes):
        self.nodes = nodes # Representing root as well
        # Instantiates the number of arrays representing every edge between each node
        self.tree_map = [TreeNode(i) for i in range(nodes)]

    def add_edge(self, x, *y):
        # Assignment of both to each other makes them linked
        for ele in range(len(y)):
            self.tree_map[x].children.append(y[ele])
            self.tree_map[x].children[ele].parent = x

    def dfs_search(self, start, end):
        explored = Stack(self.nodes)
        considered = Stack(self.nodes)

        # Root node already has been explored by default
        explored.push(0)

        def dfs_check(self, )

        # Going through each node in the tree
        for i in range(len(self.tree_map)):
            for j in range(len(explored.stack)):
                if explored.stack[j] != self.tree_map[i]:
                    # If the node has children
                    if len(self.tree_map[i].children) == 0:
                        break
                    else:
                        # Puts each node into the consideration stack
                        for node in self.tree_map[i].children:
                            considered.push(self.tree_map[node].data)

                        explored = considered.pop()

        # I'm not completely sure if this works
        for i in range(len(explored.stack)):
            print(explored.stack[i])
    
    def bsf_search(self, start, end):
        pass

    def print(self):
        pass
    
brain = Tree(10)
brain.add_edge(1, 2, 3)
brain.add_edge(2, 4, 5)
brain.add_edge(3, 6, 7, 8, 9)
brain.add_edge(5, 10)

brain.dfs_search(0, 0)