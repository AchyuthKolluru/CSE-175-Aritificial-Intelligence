#
# bfs.py
#
# This file provides a function implementing breadth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#


from route import Node
from route import Frontier


def BFS(problem, repeat_check=False):
    """Perform breadth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    #Initialize the root node
    solNode = Node(problem.start)
    
    # We want a FIFO for the Frontier so we set it to FALSE
    arr = Frontier(solNode, queue=True)
    visited = set()
    visited.add(solNode)
    
    if problem.is_goal(solNode.loc):
        # Check if starting node is the goal
        return solNode
    while not arr.is_empty():
        #if the frontier is not empty pop the leaf node
        solNode = arr.pop()
        # Check if the goals is in the Node
        if problem.is_goal(solNode.loc):
            return solNode
        # We check iterate through all possible locations through the node
        for x in solNode.expand(problem):
            if not repeat_check:
                arr.add(x)
            # Check if it is in visited set
            if x not in visited:
                visited.add(x)
                # We only want to check the repeated check to True when we 
                if repeat_check == True:
                    arr.add(x)
                
                
    return None