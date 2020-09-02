'''
The traveling salesman problem (TSP) is as follows: 

Given a list of cities and a table of distances from each city to the others,
find a shortest circuit that visits each city exactly once and returns to the
starting city.

Principle:

Suppose it is required to minimize an objective function. Suppose that
we have a method for getting a lower bound on the cost of any solution among
those in the set of solutions represented by some subset. If the best solution
found so far costs less than the lower bound for this subset, we need not
explore this subset at all. 

Cost matrix : 

C(i,j) = W(i,j) if there is a direct path from ni to nj
       = INFINITY if there is no direct path from ni to cj

A Lower Bound for a TSP：

In general, to get the lower bound of the path starting from the node, we reduce
each row and column in such a way that there must be at least one zero in each
row and Column. For doing this, we need to reduce the minimum value from each
element in each row and column. The total expected cost at the node is the sum
of all reductions. We try to calculate lower bound of the path starting at node
1 using above resulting cost matrix. The lower bound is 0 as matrix is already
in reduced form. i.e. all rows and all columns have zero values
The cost will be : cost of parent + cost of the edge(parent,current) + lower
bound of the path starting at node 1
'''
import sys 
from queue import PriorityQueue
import copy

class Node():
    def __init__(self,N):
        self.cost = 0
        # Node structure
        self.parent = None 
        self.level = -1
        self.vertex = -1
        # res : rest of the node to be selected : [0,0...0]
        self.selected = [0] * N
        # Each node has its reduced matrixs 
        self.reduced = [[0] * N] * N
    
    # return reduce costs 
    def reduce_matrix(self,M: list):
        temp = copy.deepcopy(M)
        tot_c = 0
        # reduce row : subtract minimum each row 
        for i,r in enumerate(temp):
            m = min(r)
            if (m != sys.maxsize):
                tot_c = tot_c + m
                temp[i] = [x-m if (x!=sys.maxsize) else x for x in r]
        # reduce column : subtract minimum each column
        # swap column and row 
        temp = list(map(list, zip(*temp)))
        for i,r in enumerate(temp):
            m = min(r)
            if (m != sys.maxsize):
                tot_c = tot_c + m
                temp[i] = [x-m if (x!=sys.maxsize) else x for x in r]
        self.reduced = list(map(list, zip(*temp)))
        self.cost = tot_c

    def __lt__(self, other):
        return (self.cost<=other.cost)
    
    def __eq__(self,other):
        return (self.cost == other.cost)

class Tsp():
    def __init__(self,N):
        # a table of distances from each city to the others
        self.N = N
        self.distances = [[0] * N] * N
        self.smallest = [-1]*N
        self.bound = sys.maxsize

    def set_dist(self,distances):
        self.distances = distances

    def is_safe(self,node:Node):
        if (node.cost>self.bound):
            return False
        return True 

    def find_shortest_path(self):
        Tree = PriorityQueue()
        dummynode = Node(self.N)
        # Initially start at first vertex  
        dummynode.selected[0] = 1 
        dummynode.reduce_matrix(self.distances)
        dummynode.level = 0
        dummynode.vertex = 0
        Tree.put(dummynode)
        while(not Tree.empty()):
            current = Tree.get()
            if (self.is_safe(current)):
                # if leaf node 
                if (current.level == (self.N-1)):
                    self.bound = current.cost 
                    solution = []
                    temp = current
                    while(temp):
                        solution.append(temp.vertex)
                        temp = temp.parent 
                    self.smallest = solution[::-1]
                else:  
                    for i,v in enumerate(current.selected):
                        if(v != 1):
                            next_n = Node(self.N)
                            next_n.selected = current.selected[:]
                            next_n.selected[i] = 1
                            temp = copy.deepcopy(current.reduced)
                            temp[current.vertex] = [sys.maxsize]*self.N
                            for j in range(self.N):
                                temp[j][i] = sys.maxsize
                            previous = current
                            while(previous):
                                temp[i][previous.vertex] = sys.maxsize
                                previous = previous.parent
                            next_n.reduce_matrix(temp)
                            next_n.cost = next_n.cost + current.cost + current.reduced[current.vertex][i]
                            next_n.level = current.level + 1
                            next_n.vertex = i
                            next_n.parent = current
                            Tree.put(next_n)



        


if __name__ == "__main__":
    tsp = Tsp(5)
    INFINITY = sys.maxsize
    tsp.set_dist([[INFINITY,20,30,10,11],[15,INFINITY,16,4,2],[3,5,INFINITY,2,4],[19,6,18,INFINITY,3],[16,4,7,16,INFINITY]])
    tsp.find_shortest_path()
    print(tsp.bound)
    print(tsp.smallest)

    
