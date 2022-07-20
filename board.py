
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
def illegal(board, symbol_1, symbol_2, row, column):
                print("The square you picked is already filled. Choose another.")
                
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
              
def isWinner(board, symbol_1, symbol_2, count):
                winner = True
                for row in range (0,3):
                  if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
                    winner == False
                    print("Player " + symbol_1 + ", You Won!")
                  elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
                    winner == False
                    print("Player " + symbol_2 + ", Youn Won!")
                
                for col in range (0, 3):
                  if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
                    winner = False
                    print("Player " + symbol_1 + ", You Won!")
                elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
                    winner = False
                    print("Player " + symbol_2 + ", You Won!")
                
                if board[0][0] == board[1][1] == board[2][2] == symbol_1:
                  winner = False
                  print("Player " + symbol_1 + ", You Won!")
                elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
                  winner = False
                  print("Player " + symbol_2 + ", You Won!")
                elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
                  winner = False
                  print("Player " + symbol_1 + ", You Won!")
                elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
                  winner = False
                  print("Player " + symbol_2 + ", You Won!")
                return winner

def report(count, winner, symbol_1, symbol_2):
                print("\n")
                input("Press enter to see game summary")
                if (winner == False) and (count % 2 ==1 ):
                  print("Winner : Player " + symbol_1 + ".")
                elif (winner == False) and (count % 2 == 0 ):
                  print("Winner : Player " + symbol_2 + ".")
                else:
                  print("There is a tie. ")
                
main()

                
                
                
                                   
                
                           
          

          
  
          
         
          
