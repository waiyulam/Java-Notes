#!/bin/python 
'''
0/1 Knapsack problem using BnB 
Def: Given n items with Benfits b1,b2,b3,... bn and Weights w1,w2...wn. And
maximum capacity of knapsack M.

Objectives: Find the items that should be chosen that maximises benefit. (i.e
you can either choose or not choose item m)


Branch and Bound 
The backtracking based solution works better thanbrute force by ignoring
infeasible solutions. We can do better (than backtracking) if we know a bound on
best possible solution subtree rooted with every node. If the best in subtree is
worse than current best, we can simply ignore this node and its subtrees. So we
compute bound (best solution) for every node and compare the bound with current
best solution before exploring the node.

How to find bound for every node for 0/1 Knapsack?
The idea is to use the fact that the Greedy approach provides the best solution
for Fractional Knapsack problem. To check if a particular node can give us a
better solution or not, we compute the optimal solution (through the node) using
Greedy approach. If the solution computed by Greedy approach itself is more than
the best so far, then we can’t get a better solution through the node.

Illustration 
Input:
// First thing in every pair is weight of item and second thing is value of item
Item arr[] = {{2, 40}, {3.14, 50}, {1.98, 100},{5, 95}, {3, 30}};
Knapsack Capacity W = 10

Output:
The maximum possible profit = 235

Items are considered sorted by value/weight.

This solution using iterative and priority queue , rather than recursive method.
The reason why i didn't use recursive is because we should always keep nodes for
different level.  I didn't figure out how to do this recursively
'''
import sys 
from queue import PriorityQueue


class Node():
    def __init__(self,N):
        self.cost = 0
        self.upper = 0
        self.total_weight = 0
        # The solution so far : append
        self.paths = [1]*N
        self.level = -1
    
    # Compute the bound of this node 
    # Bound is the actual cost 
    def setBound(self,weights,profits,capacity):
        totBound = 0
        r = capacity
        for i,x in enumerate(self.paths):
            if (r<=0):
                break
            if (x != 0):
                if (r>=weights[i]):
                    totBound += profits[i]
                    r = r - weights[i]
                else:
                    break
        # Return negative for converting maximization to minimization 
        self.upper =  -totBound


    # Compute the cost of this node 
    # Cost is the best possible value for using greedy -> fractional 
    # The intuition is that if cost > upper, then it is meaningless to explore the cost while there is some other node definitely has better answer than this.
    def setCost(self,weights,profits,capacity):
        totCost = 0
        r = capacity

        for i,x in enumerate(self.paths):
            if (r<=0):
                break
            if (x != 0):
                if (r>=weights[i]):
                    totCost += profits[i]
                    r = r - weights[i]
                else:
                    totCost += r * (profits[i] / weights[i])
                    r = r - r 
        self.cost =  -totCost
    
    def setWeight(self,weights):
        self.total_weight = sum ([weights[i] for i in range(0,self.level+1) if (self.paths[i] == 1)])


    def __lt__(self, other):
        return (self.cost<=other.cost)
    
    def __eq__(self,other):
        return (self.cost == other.cost)

class Knapsack():
    # n is the number of items to select 
    def __init__(self,n):
        # upperBound in decision tree 
        self.upperBound = sys.maxsize
        # One by one extract an node with minimum cost from decision tree 
        # Compute profit of all children of extracted item 
        # and keep saving maxProfit and path lead to maxProfit 
        self.maxProfit = -sys.maxsize
        self.maxSelections = None
        # Keep the size of items and items 
        self.N = n
        self.weights = [0]*n
        self.profits = [0]*n

    # Check the node is valid before it explore 
    # The node is valid if its total weights is less than the capacity and its cost is less than or equal to upper 
    def isSafe(self,capacity: int,n: Node):
        if (n.cost > self.upperBound):
            return False 
        elif (n.total_weight > capacity):
            return False 
        return True 

    # m is the capasity of knapsack
    def knapsackMax(self,weights,profits,capacity):
        Tree = PriorityQueue()
        self.weights = weights
        self.profits = profits 
        dummyNode = Node(self.N)
        dummyNode.level = -1
        dummyNode.setWeight(weights)
        dummyNode.setCost(weights,profits,capacity)
        Tree.put(dummyNode)
        while(not Tree.empty()):
            current = Tree.get()
            if (self.isSafe(capacity,current)):
                # Leaf node : path completed -> compared with saved max profits and paths
                if (current.level == (self.N-1)):
                    # compute the total profits 
                    total_profits = sum([profits[i] for i in range(0,current.level+1) if current.paths[i] == 1])
                    if (total_profits > self.maxProfit):
                        self.maxSelections = current.paths
                        self.maxProfit = total_profits
                else:
                    current.setBound(weights,profits,capacity)
                    # Update the upper bound 
                    if (current.upper < self.upperBound):
                        self.upperBound = current.upper
                    # Explore the node for all childrens 
                    for i in range(0,2):
                        next_node = Node(self.N)
                        next_node.level = current.level + 1
                        next_node.paths = [p for p in current.paths]
                        next_node.paths[next_node.level] = i 
                        next_node.setWeight(weights)
                        next_node.setCost(weights,profits,capacity)
                        Tree.put(next_node)     

if __name__ == "__main__":
    k = Knapsack(4)
    k.knapsackMax([2,4,6,9],[10,10,12,18],15)
    if (k.maxSelections != None):
        print(k.maxSelections)
        print(k.maxProfit)
    else:
        print("Solutions not existed")
    
    k2 = Knapsack(5)
    k2.knapsackMax([2,3.14,1.98,5,3],[40,50,100,95,30],10)
    if (k2.maxSelections != None):
        print(k2.maxSelections)
        print(k2.maxProfit)
    else:
        print("Solutions not existed")




''' 
Priority Queue example:
https://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
https://stackoverflow.com/questions/43481158/typeerror-not-supported-between-instances-of-state-and-state-python-3 
'''



