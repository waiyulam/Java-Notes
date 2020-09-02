#!/bin/python 
''' 
M Coloring Problem 
Given an undirected graph and a number m, determine if the
graph can be coloured with at most m colours such that no two adjacent vertices
of the graph are colored with the same color. Here coloring of a graph means the
assignment of colors to all vertices. 

Input-Output format:
 Input:
A 2D array graph[V][V] where V is the number of vertices in graph and
graph[V][V] is adjacency matrix representation of the graph. A value graph[i][j]
is 1 if there is a direct edge from i to j, otherwise graph[i][j] is 0. 
An integer m which is the maximum number of colors that can be used. 

Output: 
An array color[V] that should have numbers from 1 to m. color[i] should represent
the color assigned to the ith vertex. The code should also return false if the
graph cannot be colored with m colors.

Naive Approach: Generate all possible configurations of colours. Since each node
can be coloured using any of the m available colours, the total number of colour
configurations possible are m^V. After generating a configuration of colour,
check if the adjacent vertices have the same colour or not. If the conditions
are met, print the combination and break the loop.

Backtracking solutions: 
Approach: 
The idea is to assign colors one by one to different vertices,
starting from the vertex 0. Before assigning a color, check for safety by
considering already assigned colors to the adjacent vertices i.e check if the
adjacent vertices have the same color or not. if there is any color assignment
that does not violate the conditions, mark the color assignment as part of the
solution. If no assignment of color is possible then backtrack and return false.

Complexity analysis: 
- Time Complexity:O(m^V). There are total O(m^V) combination of colors. So time
  complexity is O(m^V). The upperbound time complexity remains the same but the
  average time taken will be less.
- Space Complexity:O(V). To store the output array O(V) space is required.

Bounding function : 
By coloring the vertices with following colors, adjacent
vertices does not have same colors

Input:  
graph = {0, 1, 1, 1},
        {1, 0, 1, 0},
        {1, 1, 0, 1},
        {1, 0, 1, 0}
Output: 
Solution Exists: Following are the assigned colors
 1  2  3  2

Input: 
graph = {1, 1, 1, 1},
        {1, 1, 1, 1},
        {1, 1, 1, 1},
        {1, 1, 1, 1}
Output: Solution does not exist.
'''
class Graph():
    def __init__(self,vertices):
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 
  
    # A utility function to check if the current color assignment 
    # is safe for vertex v 
    def isSafe(self, v, colour, c): 
        # Find the colored neighbours of vertex v 
        neighbours = [i for i in range(0,v) if self.graph[v][i] == 1]
        for n in neighbours:
            # Check if its neighbours has been colored and had same color as its neighbours 
            if (colour[n] == c):
                return False 
        return True
         

    # A recursive utility function to solve m 
    # coloring  problem 
    def graphColourUtil(self, m, colour, v):
        # base case : all nodes has been colored 
        if (v == self.V):
            return True 
        for c in range(1,m+1):
            if (self.isSafe(v,colour,c)):
                colour[v] = c
                if (self.graphColourUtil(m,colour,v+1)):
                    return True 
                else:
                    colour[v] = 0
        return False

    def graphColouring(self, m): 
        colour = [0] * self.V 
        if self.graphColourUtil(m, colour, 0) == False: 
            print ("Solution does not exist.")
            return False
  
        # Print the solution 
        print ("Solution exist and Following are the assigned colours:")
        for c in colour: 
            print(c,end="  ")
        print("\n")
        return True

if __name__ == "__main__":
    # Driver Code 
    g  = Graph(4) 
    g.graph = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]] 
    m=3
    g.graphColouring(m) 
     # Driver Code 
    g  = Graph(4) 
    g.graph = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]] 
    m=3
    g.graphColouring(m) 
    