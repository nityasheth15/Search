# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
from util import Stack
from util import Queue
from util import PriorityQueue
from __builtin__ import int



"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
  
    stack = Stack(); parentNode = []; successors = []; visitedNodes = []
    parentChildMapList = {}
    stack.push(problem.getStartState())
    currentState = problem.getStartState() #need to remove
    while problem.isGoalState(currentState) is False and problem.isGoalState(currentState[0]) is False:
        if(currentState == problem.getStartState()):
            successors = problem.getSuccessors(currentState)
            visitedNodes.append(currentState)
        else:
            successors = problem.getSuccessors(currentState[0])
            visitedNodes.append(currentState[0])
        if successors != None and len(successors) > 0 :
            parentNode.append(currentState)
        for node in successors:
            if(visitedNodes.__contains__(node) == False and visitedNodes.__contains__(node[0]) == False):
                stack.push(node)
                parentChildMapList[node] = currentState
        
        tempCurrentNode = stack.pop()
        if(visitedNodes.__contains__(tempCurrentNode) == False and visitedNodes.__contains__(tempCurrentNode[0]) == False):
            currentState = tempCurrentNode
        else:
            currentState = stack.pop()
            
    validDirections = []
    firstState = currentState
    while firstState != problem.getStartState():
        validDirections.append(firstState[1])
        firstState = parentChildMapList[firstState]

    validDirections.reverse()
    return validDirections
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    queue = Queue() ; parentNode = []; successors = []; visitedNodes = []
    parentChildMapList = {}
    currentState = problem.getStartState() #need to remove
    while problem.isGoalState(currentState) is False and problem.isGoalState(currentState[0]) is False:
        if(currentState == problem.getStartState()):
            successors = problem.getSuccessors(currentState)
            visitedNodes.append(currentState)
            visitedNodes.append((currentState, ()))
        else:
            successors = problem.getSuccessors(currentState[0])
            visitedNodes.append(currentState[0])
        if successors != None and len(successors) > 0:
            parentNode.append(currentState)
        for node in successors:
            if(visitedNodes.__contains__(node) == False and visitedNodes.__contains__(node[0]) == False):
                queue.push(node)
                parentChildMapList[node] = currentState
        tempNode = queue.pop()
        if((visitedNodes.__contains__(tempNode) == False and visitedNodes.__contains__(tempNode[0]) == False)):
            currentState = tempNode
        else:
            currentState = queue.pop()
            
    validDirections = []
    firstState = currentState


    while firstState != problem.getStartState():
            validDirections.append(firstState[1])
            firstState = parentChildMapList[firstState]
            
        
    validDirections.reverse()
    return validDirections
    util.raiseNotDefined()


def uniformCostSearch(problem):
    pQueue = PriorityQueue(); parentNode = []; successors = []; visitedNodes = []
    parentChildMapList = {}; isNodeProcessable = True
    
    if(isinstance(problem.getStartState()[0], int) or isinstance(problem.getStartState()[0], str) ):
        startState = (problem.getStartState(), 'Start State', 0)
    else:
        startState = (problem.getStartState(), problem.getStartState()[1])
        isNodeProcessable = False
    currentState = startState
    
    while (problem.isGoalState(currentState[0]) is False and (isNodeProcessable is False or problem.isGoalState(currentState) is False)):
        successors = problem.getSuccessors(currentState[0])
        visitedNodes.append(currentState[0])
        if successors != None and len(successors) > 0 :
            parentNode.append(currentState)
        for node in successors:
            if(visitedNodes.__contains__(node) == False and visitedNodes.__contains__(node[0]) == False):
                parentChildMapList[node] = currentState
                costToNode = 0
                tempStartNode = node
                while(tempStartNode != startState):
                    costToNode +=  tempStartNode[2]
                    tempStartNode = parentChildMapList[tempStartNode]
                pQueue.push(node,costToNode)
        tempNode = pQueue.pop()
        if visitedNodes.__contains__(tempNode) == False and visitedNodes.__contains__(tempNode[0]) == False:
            currentState = tempNode
        else:
            currentState = pQueue.pop()

    validDirections = []
    firstState = currentState
    while firstState != startState:
        validDirections.append(firstState[1])
        firstState = parentChildMapList[firstState]

    validDirections.reverse()
    return validDirections
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    pQueue = PriorityQueue(); parentNode = []; successors = []; visitedNodes = []
    parentChildMapList = {}; isNodeProcessable = True
    
    if(isinstance(problem.getStartState()[0], int) or isinstance(problem.getStartState()[0], str) ):
        startState = (problem.getStartState(), 'Start State', 0)
    else:
        startState = (problem.getStartState(), problem.getStartState()[1])
        isNodeProcessable = False
    currentState = startState
    
    while (problem.isGoalState(currentState[0]) is False and (isNodeProcessable is False or problem.isGoalState(currentState) is False)):
        successors = problem.getSuccessors(currentState[0])
        visitedNodes.append(currentState[0])
        if successors != None and len(successors) > 0 :
            parentNode.append(currentState)
        for node in successors:
            if(visitedNodes.__contains__(node) == False and visitedNodes.__contains__(node[0]) == False):
                parentChildMapList[node] = currentState
                costToNode = 0
                tempStartNode = node
                while(tempStartNode != startState):
                    costToNode +=  tempStartNode[2]
                    tempStartNode = parentChildMapList[tempStartNode]
                costToNode += heuristic(node[0], problem)
                pQueue.push(node,costToNode)
        tempNode = pQueue.pop()
        if visitedNodes.__contains__(tempNode) == False and visitedNodes.__contains__(tempNode[0]) == False:
            currentState = tempNode
        else:
            currentState = pQueue.pop()

    validDirections = []
    firstState = currentState
    while firstState != startState:
        validDirections.append(firstState[1])
        firstState = parentChildMapList[firstState]

    validDirections.reverse()
    return validDirections
    util.raiseNotDefined()
    util.raiseNotDefined()


# Abbreviations

bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
