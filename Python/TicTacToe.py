setup = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def want_to_play():
  response = input("Want to play TicTacToe(Yes/No)? ")
  if response == 'Yes':
    return True
  else:
    return False

def print_board(board):
  print(' {} | {} | {} '.format(board[6],board[7],board[8]))
  print('---|---|---')
  print(' {} | {} | {} '.format(board[3],board[4],board[5]))
  print('---|---|---')
  print(' {} | {} | {} '.format(board[0],board[1],board[2]))

def get_move():
  return input("Input move using numpad: ")

def evaluate_move(move,t):
  outcome = False
  setup[int(move)-1] = 'O' if t else 'X'
  s = setup
  print_board(s)

  if 'XXX' in {s[0]+s[1]+s[2], s[3]+s[4]+s[5], s[6]+s[7]+s[8], s[6]+s[3]+s[0], s[7]+s[4]+s[1], s[8]+s[5]+s[2], s[0]+s[4]+s[8], s[6]+s[4]+s[2]}:
    outcome = True

  if 'OOO' in {s[0]+s[1]+s[2], s[3]+s[4]+s[5], s[6]+s[7]+s[8], s[6]+s[3]+s[0], s[7]+s[4]+s[1], s[8]+s[5]+s[2], s[0]+s[4]+s[8], s[6]+s[4]+s[2]}:
    outcome = True

  return outcome

def main():
  while True:
    if not want_to_play():
      break
    print_board(setup)
    winner = False
    turn = 0
    while not winner:
      m = get_move()
      turn += 1
      if m == '0':
        break
      elif not setup[int(m)-1] == ' ':
        print("Invalid Move")
        turn -= 1
        continue
      else:
        try:
          if evaluate_move(m,turn%2==0):
            print("WINNER")
            break
          if turn == 9:
            print("DRAW")
            break
        except:
          print("Invalid Move")

  print("Quitting")

if __name__ == "__main__":
  main()