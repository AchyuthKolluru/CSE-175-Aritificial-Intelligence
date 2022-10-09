#
# greedy.py
#
# This file provides a function implementing greedy best-first search for
# a route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier. Also, this function uses heuristic function objects defined
# in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#


from route import Node
from route import Frontier


def greedy_search(problem, h, repeat_check=False):
    """Perform greedy best-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    solNode = Node(problem.start)
    arr = Frontier(solNode, sort_by='h')
    visited = set()
    visited.add(solNode)

    if problem.is_goal(solNode.loc):
        return solNode
    while not arr.is_empty():
        solNode = arr.pop()
        if problem.is_goal(solNode.loc):
            return solNode
        for x in solNode.expand(problem):
            if repeat_check:
                if x in visited:
                    if arr.contains(x) and x.value(sort_by='g') < arr.__getitem__(x):
                        arr.__delitem__(x)
                        arr.add(x)
                else:
                    arr.add(x)
                    visited.add(x)
            else:
                arr.add(x)
                visited.add(x)


    return None
