from math import inf
import copy


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if len(actions(board)) % 2 ==0:
        return O
    else:
        return X

        
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action[0], action[1]
    if board[i][j] != EMPTY:
        raise Exception('not a valid action')
    else:
        new_board_state = copy.deepcopy(board)
        new_board_state[i][j] = player(board)
        return new_board_state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win_state = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    if [X, X, X] in win_state:
        return X
    elif [O, O, O] in win_state:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O or len(actions(board)) == 0:
        return True 
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        utility = +1
    elif winner(board) == O:
        utility = -1
    else:
        utility = 0
    return utility


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif len(actions(board)) == 9:
        return (1, 1)
    else:
        ai = player(board)
        best = max_score(board, ai)
        return (best[0], best[1])


def max_score(board, ai):
    """
    Returns list of move coordinates and maximum score.
    """
    best = [0, 0, -inf]
    if terminal(board):
        if ai == X:
            score = utility(board)
        else:
            score = -utility(board)
        return [0, 0, score]
    for action in actions(board):
        score = min_score(result(board, action), ai)
        score[0], score[1] = action[0], action[1]
        if score[2] > best[2]:
            best = score
    return best
        
        
def min_score(board, ai):
    """
    Returns list of move coordinates and minimum score.
    """
    best = [0, 0, inf]
    if terminal(board):
        if ai == X:
            score = utility(board)
        else:
            score = -utility(board)
        return [0, 0, score]
    for action in actions(board):
        score = max_score(result(board, action), ai)
        score[0], score[1] = action[0], action[1]
        if score[2] < best[2]:
            best = score
    return best
