#!/usr/bin/python3

import json


PLAYERS = (1, 2)

def load():
  fp = open('board.json')
  board = json.load(fp)
  n = len(board)
  for row in board:
    if n != len(row):
      raise ValueError("Bad dimension size")
  return board

def rows(board):
  return board

def cols(board):
  return list(zip(*board))

def diags(board):
  n = len(board)
  ascending = range(n)
  descending = reversed(ascending)
  iterators = (zip(ascending, ascending), zip(descending, ascending))
  return [[board[row][col] for row, col in iterator] for iterator in iterators]

def won(player, paths):
  for path in paths:
    same = map(lambda p: player == p, path)
    if all(same):
      return True
  return False

def rate(board):
  paths = rows(board) + cols(board) + diags(board)
  return [(player, won(player, paths)) for player in PLAYERS]

if __name__ == '__main__':
  board = load()
  print(board)
  state = rate(board)
  print(state)

