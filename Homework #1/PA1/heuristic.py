#
# heuristic.py
#
# This script defines a utility class that can be used as an implementation
# of a frontier state (location) evaluation function for use in route-finding
# heuristic search algorithms. When a HeuristicSearch object is created,
# initialization code can be executed to prepare for the use of the heuristic
# during search. In particular, a RouteProblem object is typically provided 
# when the HeuristicFunction is created, providing information potentially
# useful for initialization. The actual heuristic cost function, simply
# called "h_cost", takes a state (location) as an argument.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#


import route


class HeuristicFunction:
    """A heuristic function object contains the information needed to
    evaluate a state (location) in terms of its proximity to an optimal
    goal state."""

    def __init__(self, problem=None):
        self.problem = problem
        
        # PLACE ANY INITIALIZATION CODE HERE
    def h_cost(self, loc=None):
        """An admissible heuristic function, estimating the cost from
        the specified location to the goal state of the problem."""
        # a heuristic value of zero is admissible but not informative
        value = 0.0
        if loc is None:
            return value
        else:
            # PLACE YOUR CODE FOR CALCULATING value OF loc HERE
            # An admissable heurisitic function can be determined through the euclidian distance to get an estimate.
            #gets the goal location of the problem
            # goalLoc = self.problem.goal
            
            all_streets = self.problem.actions(loc)
            # print(all_streets)
            speed = []
            for roads in all_streets:
                
                places = self.problem.result(loc, roads)
                time_cost = self.problem.action_cost(loc, places)
                distance = self.problem.map.euclidean_distance(loc, places)
                speed.append(distance/time_cost)
            
            
            #figures out the euclidian value from 2 locations goalLoc and the value that is being passed in 
            # print(self.problem.map.euclidean_distance(loc, goalLoc))
            value = min(speed)
            return value

