# This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, == Part 4.

# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space, == a 2 means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, == tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

# Here are some more examples to work with:

# winner_is_2 = [[2, 2, 0],
#       	[2, 1, 0],
#       	[2, 1, 1]]

# winner_is_1 = [[1, 2, 0],
#       	[2, 1, 0],
#       	[2, 1, 1]]

# winner_is_also_1 = [[0, 1, 0],
# 	                 [2, 1, 0],
# 	                 [2, 1, 1]]

# no_winner = [[1, 2, 0],
# 	        [2, 1, 0],
#       	[2, 1, 2]]

# also_no_winner = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 0]]

def winner(li):
    if li[0][0] == li[0][1] == li[0][2]:
        print(f'player {li[0][0]} won')
    elif li[1][0] == li[1][1] == li[1][2]:
        print(f'player {li[1][0]} won')
    elif li[2][0] == li[2][1] == li[2][2]:
        print(f'player {li[2][0]} won')

    elif li[0][0] == li[1][0] == li[2][0]:
        print(f'player {li[0][0]} won')
    elif li[0][1] == li[1][1] == li[2][1]:
        print(f'player {li[0][1]} won')
    elif li[0][2] == li[1][2] == li[2][2]:
        print(f'player {li[0][2]} won')

    elif li[0][0] == li[1][1] == li[2][2]:
        print(f'player {li[0][0]} won')
    elif li[0][2] == li[1][1] == li[2][0]:
        print(f'player {li[0][2]} won')

    else:
        print('no winner')

winner(winner_is_2)
winner(winner_is_1)
winner(game)
winner(winner_is_also_1)
winner(no_winner)
winner(also_no_winner)