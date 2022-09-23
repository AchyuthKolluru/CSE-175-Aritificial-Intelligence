#
# dfs.py
#
# This file provides a function implementing depth-first search for a
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
from route import RouteProblem


def DFS(problem: RouteProblem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    print(problem.start)
    solNode = Node(problem.start)
    print(solNode.expand(problem))

    

    return None
