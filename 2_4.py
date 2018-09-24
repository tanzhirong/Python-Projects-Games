"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    max_score = 0
    for dice in hand:
        result = list(hand).count(dice)*dice
        if result > max_score:
            max_score = result
    #return the max score you can get from a hand
    return max_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = set(range(1, num_die_sides + 1))
    all_rolls = gen_all_sequences(outcomes, num_free_dice)
    total = 0
    for a_set in all_rolls:
        total += score(a_set + held_dice)
    return float(total)/len(all_rolls)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.
    hand: full yahtzee hand
    Returns a set of tuples, where each tuple is dice to hold
    """
    all_holds = set([()])
    #For each dice in the hand, look at possible permutations
    for dice in hand: 
        temp_holds = all_holds.copy()
        for item in temp_holds:
            new_seq = list(item)
            new_seq.append(dice)
            #turn into tuple, try add into set to avoid duplicates
            all_holds.add(tuple(new_seq))
    return all_holds


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = gen_all_holds(hand)
    best_value = 0.0
    best_hold = tuple([])
    for hold in all_holds:
        temp_value = expected_value(hold, num_die_sides, len(hand)-len(hold))
        if temp_value > best_value:
            best_value = temp_value
            best_hold = hold
    return (best_value, best_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 5, 5)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       