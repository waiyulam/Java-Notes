#!/bin/python
'''hamitonian cycle problem using backtracking 
Hamiltonian Path in an undirected graph is a path that visits each vertex
exactly once. A Hamiltonian cycle (or Hamiltonian circuit) is a Hamiltonian Path
such that there is an edge (in the graph) from the last vertex to the first
vertex of the Hamiltonian Path. Determine whether a given graph contains
Hamiltonian Cycle or not. If it contains, then prints the path. Following are
the input and output of the required function.

Input: 
A 2D array graph[V][V] where V is the number of vertices in graph and
graph[V][V] is adjacency matrix representation of the graph. A value graph[i][j]
is 1 if there is a direct edge from i to j, otherwise graph[i][j] is 0.

Output: 
List all possible hamiltonian path in graph. An array path[V] that should contain the Hamiltonian Path. path[i]
should represent the ith vertex in the Hamiltonian Path. The code should also
return false if there is no Hamiltonian Cycle in the graph.

Naive Algorithm: 
Generate all possible configurations of vertices and print a
configuration that satisfies the given constraints. There will be n! (n
factorial) configurations.

Backtracking Algorithm: 
Create an empty path array and add vertex 0 to it. Add
other vertices, starting from the vertex 1. Before adding a vertex, check for
whether it is adjacent to the previously added vertex and not already added. If
we find such a vertex, we add the vertex as part of the solution. If we do not
find a vertex then we return false.

Time complexity :
Worst case complexity of using DFS and backtracking is O(N!).
'''
import sys
class Graph():  
    def __init__(self, vertices):  
        self.graph = [[0 for column in range(vertices)] 
                            for row in range(vertices)] 
        self.paths = []
        self.V = vertices  
  
    ''' Check if this vertex is an adjacent vertex  
        of the previously added vertex and is not  
        included in the path earlier '''
    def isSafe(self, v, pos, path):
        # check if there is valid edge to the last vertex in path 
        if (self.graph[path[pos-1]][v] == 0):
            return False 
        # Check if vertex is already included in path to avoid duplicate node 
        for i in range(0,pos):
            if v == path[i]:
                return False 
        return True 

  
    # A recursive utility function to solve  hamiltonian cycle problem  
    # param pos : next empty spot 
    def hamCycleUtil(self, path, pos):  
        # Base case : if all vertices included in the path 
        if pos == self.V:
            # last vertex must be adjacent to first vertex in path to make a cyle  
            if self.graph[path[pos-1]][path[0]] == 1:
                temp = [v for v in path]
                self.paths.append(temp)
        else:
            # Try different vertices as a next candidate  
            # in Hamiltonian Cycle.
            for v in range(0,self.V): 
                if (self.isSafe(v,pos,path)):
                    path[pos] = v
                    self.hamCycleUtil(path,pos+1)
                    # IMPORTANT: Kill current vertex if it doesn't  lead to a solution 
                    # This is elegant although it would not lead to unexpected behavior if not include this line)
                    path[pos] = -1
        return 
        
  
    def hamCycle(self):  
        path = [-1] * self.V  
        ''' Let us put vertex 0 as the first vertex  
            in the path. If there is a Hamiltonian Cycle,  
            then the path can be started from any point  
            of the cycle as the graph is undirected '''
        path[0] = 0
        self.hamCycleUtil(path,1)

        if len(self.paths) == 0:  
            print ("Solution does not exist\n") 
            return False
        print ("Solution Exists : Following are all possible Hamiltonian Cycles") 
        for path in self.paths:
            self.printSolution(path)  
        return True
  
    def printSolution(self, path):  
        for vertex in path:  
            print (vertex+1, end = " ") 
        print (path[0]+1, "\n") 


if __name__ == "__main__":
    g1 = Graph(5)  
    g1.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],  
            [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],  
            [0, 1, 1, 1, 0], ] 
    g1.hamCycle()

    g3 = Graph(6)  
    g3.graph = [[0,1,1,0,0,1],[1,0,1,0,1,1,],[1,1,0,1,0,0],[0,0,1,0,1,0],[0,1,0,1,0,1],[1,1,0,0,1,0]]
    g3.hamCycle()

    g2 = Graph(5)  
    g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],  
        [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],  
        [0, 1, 1, 0, 0], ]
    g2.hamCycle();  


'''
Note: Note that the above code always prints cycle starting from 0. The starting
point should not matter as the cycle can be started from any point. If you want
to change the starting point, you should make two changes to the above code.
Change “path[0] = 0;” to “path[0] = s;” where s is your new starting point. Also
change loop “for (int v = 1; v < V; v++)" in hamCycleUtil() to "for (int v = 0;
v < V; v++)".
'''