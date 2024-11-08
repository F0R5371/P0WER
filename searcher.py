import stats

class Stack:
    def __init__(self, max):
        self.max = max
        self.top = -1
        self.stack = [-1] * max

    def push(self, value):
        if self.top == self.max - 1:
            print(f'{value} failed to push.')
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
        
    def peek(self):
        if self.empty():
            return
        
        return self.stack[self.top]

    def print(self):
        print(self.stack[0:self.top + 1])

    def tree_print(self):
        if self.empty():
            print('Nothing to be printed.')
            return

        for i in range(self.top + 1):
            if (i == self.top):
                print(self.stack[i], end = " ")
            else:
                print(self.stack[i], end = " -> ")
        print()

class Queue:
    def __init__(self, max):
        self.max = max
        self.rear = -1
        self.front = -1
        self.queue = [-1] * max

    def enqueue(self, value):
        if self.front == self.max - 1:
            print(f'{value} failed to enqueue.')
            return
        
        # In other words rear value is being initialized
        if self.empty():
            self.rear += 1

        self.front += 1
        self.queue[self.front] = value

    def dequeue(self):
        if self.empty():
            return
        
        dequeue_num = self.rear
        self.rear += 1

        if self.rear - 1 == self.front:
            self.rear = -1
            self.front = -1

        return self.queue[dequeue_num]

    def empty(self):
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False
        
    def peek(self):
        if self.empty():
            return

        return self.queue[self.front]

    def print(self):
        print(self.queue[self.rear:self.front + 1])

    def tree_print(self):
        if self.empty():
            print('Nothing to be printed.')
            return

        for i in range(self.rear, self.front + 1):
            if i == self.front:
                print(self.queue[i], end = ' ')
            else:
                print(self.queue[i], end = ' -> ')
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
        explored = Stack(self.nodes + 1)
        considered = Stack(self.nodes + 1)

        # If start is 0, then the root node has already been explored
        explored.push(start)

        # How many times AI ran function, determines efficiency
        global count
        count = 0

        def dfs_check():
            global count
            count += 1
            next = explored.peek()
            if next == end:
                return
            if len(self.tree_map[next].children) == 0 and considered.empty():
                return
            else:
                for child in self.tree_map[next].children:
                    # Pushs only the numbers and not a TreeNode class itself
                    considered.push(child)

                # Pops a node out of considered and explores it
                explored.push(considered.pop())
                dfs_check()
        dfs_check()

        # Statistics
        # For every dfs search you run, data about it will be created
        stats.x_vals.append(self.nodes + 1)
        stats.y_vals.append(count)

        if explored.peek() != end:
            raise RuntimeError('Could not find a solution!')
        
        # Return explored
        explored.tree_print()
    
    def bsf_search(self, start, end):
        explored = Queue(self.nodes + 1)
        considered = Queue(self.nodes + 1)

        explored.enqueue(start)

        def bfs_check():
            next = explored.peek()
            if next == end:
                return
            if len(self.tree_map[next].children) == 0 and considered.empty():
                return
            else:
                for child in self.tree_map[next].children:
                    considered.enqueue(child)

                explored.enqueue(considered.dequeue())
                bfs_check()
        bfs_check()

        if explored.peek() != end:
            raise RuntimeError('Could not find a solution!')
        
        explored.tree_print()

    def print(self):
        for node in self.tree_map:
            for child in node.children:
                print(f'{node.data} -> {child}')
    
brain = Tree(11)
brain.add_edge(0, 1, 2)
brain.add_edge(1, 3, 4)
brain.add_edge(2, 5, 6)
brain.add_edge(3, 7, 8, 9, 10)
brain.add_edge(5, 11)

# In the future, work on timing each of these processes and use them for statistics.
for i in range(12):
    brain.dfs_search(0, i)

print('Now for the BFS search...')

for i in range(12):
    brain.bsf_search(0, i)

# Statistics