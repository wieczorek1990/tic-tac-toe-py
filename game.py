#!/usr/bin/python3

import json


def load():
  fp = open('board.json')
  return json.load(fp)

def winner(board):
  n = len(board)
  for col in board:
    if n != len(col):
      raise ValueError("Bad dimension size")

  rows = board

  cols = list(zip(*board))

  ascending = range(n)
  descending = reversed(ascending)
  iterators = (zip(ascending, ascending), zip(descending, ascending))
  diags = [[board[row][col] for row, col in iterator] for iterator in iterators]

  paths = rows + cols + diags

  for player in (1, 2):
    for path in paths:
      same = map(lambda p: player == p, path)
      if all(same):
        return player

  return 0

board = load()
print(board)
player = winner(board)
if player != 0:
  print("Player {} won".format(player))
else:
  print("No winner")

