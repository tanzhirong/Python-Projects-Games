"""
Monte Carlo Tic-Tac-Toe Player
(functions)
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# TTT Board Constants
EMPTY = 1
PLAYERX = 2
PLAYERO = 3 
DRAW = 4
    
def mc_trial(board, player):
    """
    Play TTT game with given board and player.
    And alternates between players
    """
    # Loop until game is won/lost/drawn
    while board.check_win() == None:
        empty_squares = board.get_empty_squares()
        move = random.choice(empty_squares)
        board.move(move[0], move[1], player)
        player = provided.switch_player(player)

def mc_update_scores(scores, board, player):
    """
    Update the score grid of same board dimension.
    Winning player gets incremented value while losing player gets 
    values decremented. 
    """
    winner = board.check_win()	# Check winner
    if winner in (DRAW, None):	# Return if in progress or draw
        return None
    
    # Winner increments score, loser decrements score
    curr_score  = SCORE_CURRENT  if winner == player else -SCORE_CURRENT
    other_score = -SCORE_OTHER if winner == player else SCORE_OTHER
    
    # Iterate through board and check current square and add value
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if(board.square(row,col) == player):
                scores[row][col] += curr_score
            elif(board.square(row,col) == provided.switch_player(player)):
                scores[row][col] += other_score

def get_best_move(board, scores):
    """
    Return one random empty square with the maximum score
    """
    empty_squares = board.get_empty_squares()
    empty_scores = []
    empty_max = []
    if(empty_squares == []):	# Error if this is executed
        return None
    
    # Append all scores into a list and retrieve the max score
    for row, col in empty_squares:
        empty_scores.append(scores[row][col])
    max_score = max(empty_scores)
    
    # Iterate through the empty squares and compare to max and build list
    for row, col in empty_squares:
        if(max_score == scores[row][col]):
            empty_max.append((row,col))
            
    # Return a random tuple that contains the max score value
    return random.choice(empty_max)

def mc_move(board, player, trials):
    """
    Returns a square for the machine player using Monte Carlo
    """
    # Set an empty score list of same dimensions
    scores = [[ 0 for col in range(board.get_dim())]
                  for row in range(board.get_dim())]
    for _ in range(trials):
        board_copy = board.clone()
        mc_trial(board_copy, player)
        mc_update_scores(scores, board_copy, player)
    row, col = get_best_move(board, scores)
    return row, col

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
