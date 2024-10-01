# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from heapq import heappush, heappop
from lab2_utils import TextbookStack, apply_sequence
from collections import deque
import copy

def a_star_search(stack):

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #
    # create a set of visited nodes, we can't have duplicates so use a set
    closed = []
    # create a list of nodes to visit
    open = []
    
    # calculating f value of first node
    g = 0
    h = calculate_h(stack)
    f = g + h
    # first step is to add first node
    heappush(open, (f, g, flip_sequence, stack))
    # adding an incrementor g so we heappush does not compare stacks if f is the same
    
    # while there are nodes to traverse
    while(open):
        # get the current node and remove it from open
        f, g, flip_sequence, curr_node = heappop(open)
        # if current node is visited, move to next iteration
        if curr_node in closed:
            continue
        # add current node to closed, because we visited
        closed.append(curr_node)
        # check if we reached goal node (aka correct order & orientation)
        if(curr_node.check_ordered()):
            # return correct sequence
            return flip_sequence
        # iterate through current node's neighbors
        for i in range(1, len(stack.order) + 1):
            # find the child node
            child_node = curr_node.copy()
            child_node.flip_stack(i)
            # get the sequence that led to the child node
            new_seq = flip_sequence.copy()
            new_seq.append(i)
            # calculating child node's f(n) value
            g = len(new_seq)
            f = g + calculate_h(child_node)
            # add the one node with the least f value into heappush and put in open
            heappush(open, (f, -1 * g, new_seq, child_node))
    return flip_sequence

    # ---------------------------- #

# helper function I defined to calculate h(n) value
def calculate_h(stack):
    h = 0
    for i in range(0, len(stack.order)):
        # break out of loop because we already checked last index with previous
        if(i == len(stack.order) - 1):
            break
        # checking pairs
        else:
            # 1st case: pair of books not consecutive, regardless of orientation
            nextOrder = stack.order[i+1]
            currOrder = stack.order[i]
            diff = nextOrder - currOrder
            nextOrient = stack.orientations[i+1]
            currOrient = stack.orientations[i]

            # 1st case: pair of books not consecutive, regardless of orientation
            if (abs(diff)!=1):
                h += 1
            # 2nd case: pair of books has opposite orientations
            elif(nextOrient != currOrient):
                h += 1
            # 3rd case: pair of books have correct orientation, but incorrect order
            elif((diff == -1) and 
                 ((currOrient == 1) and (nextOrient == 1))):
                h += 1
            # 4th case: pair of books have correct order, but incorrect orientation
            elif((diff == 1) and (currOrient == 0) and (nextOrient == 0)):
                h += 1
    return h

def weighted_a_star_search(stack, epsilon=None, N=1):
    # Weighted A* is extra credit

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #

    return flip_sequence

    # ---------------------------- #

