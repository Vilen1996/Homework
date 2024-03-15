# 1  Given three numbers a, b (a ≤ b) and step. Create an list of
# evenly spaced elements starting from a to b spaced by step. you
# have 3 argument

# def loop(a,b,step):
#     arr = []
#     for i in range(a, b+1, step):
#         arr.append(i)
#     return arr
#
# print(loop(1,20,2))

# 2 Imagine you and the computer are playing tennis. write a
# program where you have a sheet where victory points are
# kept and you need to figure out who is the winner.
# A set is won by the first side to win 6 games. You should to show
# the result of the match.
# If game win you in list add “a” if pc “b”.

# Example 1
#
# def game_with_pc(arr):
#     gamers_score = []
#     i = 0
#     while i < len(arr):
#         if arr[i:i+6].count('b') == 6:
#             arr = arr[i + 6:]
#             gamers_score.append('b')
#             i = 0
#         elif arr[i:i+6].count('a') == 6:
#             arr = arr[i + 6:]
#             gamers_score.append('a')
#             i = 0
#         else:
#             i += 1
#     if gamers_score.count('b') == gamers_score.count('a'):
#         return 'Draw'
#     return 'PC Wins' if gamers_score.count('b') > gamers_score.count('a') else 'I Win'
#
#
# results = ['b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
# print(game_with_pc(results))

# Example 2

# def game_with_pc(arr):
#     text = ''.join(arr)
#     return 'PC Wins' if text.count('bbbbbb') > text.count('aaaaaa') else 'I Win'
#
# results = ['b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b','b', 'a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
# print(game_with_pc(results))

# Example 3

# def game_with_pc(arr):
#     gamers_score = []
#     count = 0
#     for i in range(len(arr)-1):
#         if arr[i] == 'b':
#             count += 1
#             if count == 6:
#                 gamers_score.append('b')
#                 count = 0
#             elif arr[i+1] == 'a':
#                 count = 0
#         elif arr[i] == 'a':
#             count += 1
#             if count == 6:
#                 gamers_score.append('a')
#                 count = 0
#             elif arr[i+1] == 'b':
#                 count = 0
#     print(gamers_score)
#     if gamers_score.count('b') == gamers_score.count('a'):
#         return 'Draw'
#     return 'PC Wins' if gamers_score.count('b') > gamers_score.count('a') else 'I Win'
# 
# results = ['b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
# print(game_with_pc(results))
