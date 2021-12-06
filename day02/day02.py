input_file = 'input.txt'

def process_input():
  with open(input_file) as f:
      content = f.readlines()
  return [x.strip().split(' ') for x in content]

def part_one(directions):
  horz = 0
  vert = 0
  for pair in directions:
    val = int(pair[1])
    if pair[0] == "forward":
      horz += val
    elif pair[0] == "up":
      vert -= val
    elif pair[0] == "down":
      vert += val
  return horz * vert

def part_two(directions):
  horz = 0
  vert = 0
  aim = 0
  for pair in directions:
    val = int(pair[1])
    if pair[0] == "forward":
      horz += val
      vert += val * aim
    elif pair[0] == "up":
      aim -= val
    elif pair[0] == "down":
      aim += val
  return horz * vert

def main():
  directions = process_input()
  print(part_one(directions))
  print(part_two(directions))

if __name__ == "__main__":
  main()
