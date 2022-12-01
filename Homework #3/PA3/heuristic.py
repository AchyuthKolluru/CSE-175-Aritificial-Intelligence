#
# heuristic.py
#
# This Python script file provides two functions in support of minimax search
# using the expected value of game states. First, the file provides the
# function "expected_value_over_delays". This function takes as an argument
# a state of game play in which the current player has just selected an
# action. The function calculates the expected value of the state over all
# possible random results determining the amount of time before the
# Guardian changes gaze direction. This function calculates this value
# regardless of whose turn it is. The value of game states that result from
# different random outcomes is determined by calling "value". Second, the
# file provides a heuristic evaluation function for non-terminal game states.
# The heuristic value returned is between "max_payoff" (best for the
# computer player) and negative one times that value (best for the opponent).
# The heuristic function may be applied to any state of play. It uses
# features of the game state to predict the game payoff without performing
# any look-ahead search.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE
#
# Achyuth Kolluru 11/29/2022
#


from parameters import *
from minimax import probability_of_time
from minimax import value


def expected_value_over_delays(state, ply):
    """Calculate the expected utility over all possible randomly selected
    Guardian delay times. Return this expected utility value."""
    expected = 0
    for i in range(2, 6):
        state.time_remaining = i
        expected += probability_of_time(i) * value(state, ply)
    # PLACE YOUR CODE HERE
    # Note that the value of "ply" must be passed along, without
    # modification, to any function calls that calculate the value 
    # of a state.
    return expected


def heuristic_value(state):
    """Return an estimate of the expected payoff for the given state of
    game play without performing any look-ahead search. This value must
    be between the maximum payoff value and the additive inverse of the
    maximum payoff."""
    val = 0.0
    # PLACE YOUR CODE HERE
    
    #First we want to check if it is the Computers turn or not
    if state.current_turn == Player.west:
        #Now we want to check if the computers score is lower than the players score
        if state.e_loc <= state.w_loc:
            #if it is then we want to play safe
            val = max_payoff
        else:
            #if it isn't then we use the heuristic function
            val = (state.e_loc + state.w_loc) * (max_payoff/(max_time_steps + 1))
        val = val * -1
    else:
        if state.e_loc <= state.w_loc:
            val = -max_payoff
        else:
            val = (state.e_loc + state.w_loc) * (max_payoff/(max_time_steps + 1))
    #heuristic = (west_value + east_value) * (max_pay_off/(max_time_steps + 1))
    
    #Now we want to make sure that it is between the the inverse max payoff and the max_payof
        
    
    val = max(min(val, max_payoff), -max_payoff)
    return val
