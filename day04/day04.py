input_file = 'input.txt'

def line_to_row(line):
  return [int(x.strip()) for x in ' '.join(line.split()).split(' ')]

def process_input():
  with open(input_file) as f:
      content = f.readlines()
  numbers = [int(x.strip()) for x in content[0].split(",")]
  boards = []
  num_boards = (len(content)-1)/6
  for i in range(num_boards):
    board = []
    for j in range(1, 6):
      board.append(line_to_row(content[1 + 6 * i + j]))
    boards.append(board)

  return numbers, boards

def check_row(row):
  if row[0] == 'x' and row[0] == row[1] and row[1] == row[2] and row[2] == row[3] and row[3] == row[4]:
    return True
  return False

def check_col(board, col):
  if board[0][col] == 'x' and board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[2][col] == board[3][col] and board[3][col] == board[4][col]:
    return True
  return False

def check_diag(board):
  if board[2][2] != 'x':
    return False
  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == board[3][3] and board[3][3] == board[4][4]:
    return True
  if board[0][4] == board[1][3] and board[1][3] == board[2][2] and board[2][2] == board[3][1] and board[3][1] == board[4][0]:
    return True
  return False

def check_board(board):
  for i in range(5):
    if check_row(board[i]) or check_col(board, i):
      return True
  return check_diag(board)

def play_game(numbers, boards):
  for number in numbers:
    for board_idx, board in enumerate(boards):
      for row in board:
        for it_idx, item in enumerate(row):
          if item == number:
            row[it_idx] = 'x'
      if (check_board(board)):
        return number, board_idx

def sum_remaining(board):
  ans = 0
  for row in board:
    for item in row:
      if item != 'x':
        ans = ans + item
  return ans

def play_until_last(numbers, boards):
  complete = set()
  for number in numbers:
    for board_idx, board in enumerate(boards):
      for row in board:
        for it_idx, item in enumerate(row):
          if item == number:
            row[it_idx] = 'x'
      if (check_board(board)):
        complete.add(board_idx)
      if len(complete) == len(boards):
        return number, board_idx

def part_one(numbers, boards):
  number, winning_board = play_game(numbers, boards)
  return number * sum_remaining(boards[winning_board])

def part_two(numbers,boards):
  number, losing_board = play_until_last(numbers,boards)
  return number * sum_remaining(boards[losing_board])

def main():
  numbers, boards = process_input()
  print(part_one(numbers, boards))
  numbers, boards = process_input()
  print(part_two(numbers, boards))

if __name__ == "__main__":
  main()
