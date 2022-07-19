
def create_grid():
  print(“TIC-TAC-TOE Playboard: “)
  board = [[“ “, “ “, “ “],
           [“ “, “ “, “ “],
           [“ “, “ “, “ “]]
  return board

def main():
  introduction = intro()
  board = create_grid()
  pretty = printPretty(board)
  symbol_1, symbol_2 = sym()
  full = isFull(board, symbol_1, symbol_2)

def printPretty(board):
  rows = len(board)
  cols = len(board)
  print("---+---+---")
  for r in range(rows):
    print(board[r][0], ' |", board[r][1], " |", board[r][2])
    print("---+---+---")
  return board
          
def sym():
  symbol_1 = input("Player 1, choose X or O? ")
  if symbol_1 == "X"
      symbol_2 = "O"
      print("Player 2 is O.")
  else:
    symbol_2 = "X"
    print("Player 2 is X.")
  input("Press enter to play.")
  print("\n")
  return (symbol_1, symbol_2)
          
def startGamming(board, symbol_1, symbol_2, count):
          if count % 2 == 0:
            player = symbol_1
          elif count % 2 == 1:
            player = symbol_2
          print("Player "+ "player + ", It is your turn! ")
          row = int(input("Pick a row:"
                          "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
          column = int(input("Pick a column:"
                             "[left column: enter 0, middle column: enter 1, right column: enter 2]"))
                
while (row > 2 or row < 0) or (column > 2 or column < 0):
                outOfBoard(row, column)
                row = int(input("Pick a row:"
                                "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
                column = int(input("Pick a column:"
                                   "[left column: enter 0, middle column: enter 1, right column: enter 2]"))
while (board[row][column] == symbol_1) or (board[row][column] == symbol_2):
                filled = illegal(board, symbol_1, symbol_2, row, column)
                row = int(input("Pick a row:"
                                "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
                column = int(input("Pick a column:"
                                   "[left column: enter 0, middle column: enter 1, right column: enter 2]"))
if player == symbol_1:
                board[row][column] = symbol_1
else:
                board[row][column] = symbol_2
return (board)
                
                                   
                
                           
          

          
  
          
         
          
