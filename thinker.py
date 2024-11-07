import numpy

class Stack:
    def __init__(self, max):
        self.max = max
        self.top = -1
        self.stack = [-1] * max

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
        
    def get_top(self):
        if self.empty():
            return
        
        return self.stack[self.top]

    def print(self):
        for i in range(self.top + 1):
            if (i == self.top):
                print(self.stack[i], end = " ")
            else:
                print(self.stack[i], end = " -> ")
        print()

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

class Tree:
    def __init__(self, nodes):
        self.nodes = nodes # Representing root as well
        # Instantiates the number of arrays representing every edge between each node
        self.tree_map = [TreeNode(i) for i in range(nodes + 1)]

    def add_edge(self, x, *y):
        # Assignment of both to each other makes them linked
        for ele in y:
            self.tree_map[x].children.append(ele)
            self.tree_map[ele].parent = x

    def dfs_search(self, start, end):
        explored = Stack(self.nodes)
        considered = Stack(self.nodes)

        # If start is 0, then the root node has already been explored
        explored.push(start)

        def dfs_check():
            next = explored.get_top()
            if next == end:
                return
            if len(self.tree_map[next].children) == 0 and considered.empty():
                return
            else:
                for child in self.tree_map[next].children:
                    # Pushs only the numbers and not a TreeNode class itself
                    print(child)
                    considered.push(child)
                # Pops a node out of considered and explores it
                explored.push(considered.pop())
                dfs_check()
        dfs_check()

        if explored.get_top() != end:
            print("No solution") 
        
        # Return explored
        explored.print()
    
    def bsf_search(self, start, end):
        pass

    def print(self):
        pass
    
brain = Tree(11)
brain.add_edge(0, 1, 2)
brain.add_edge(1, 3, 4)
brain.add_edge(2, 5, 6)
brain.add_edge(3, 7, 8, 9, 10)
brain.add_edge(5, 11)

# In the future, work on timing each of these processes and use them for statistics.
brain.dfs_search(0, 7)