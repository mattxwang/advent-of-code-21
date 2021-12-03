import operator
input_file = 'input.txt'

def process_input():
  with open(input_file) as f:
      content = f.readlines()
  return [x.strip() for x in content]

def most_common_bits(readings):
  blen = len(readings[0])
  count = [0 for i in range(blen)]
  for line in readings:
    for i in range(blen):
      count[i] += int(line[i])
  most_freq = [str(int(x > len(readings)/2)) for x in count]
  return most_freq

def filter_rating(readings, op):
  blen = len(readings[0])
  valid = readings
  for i in range(blen - 1):
    if len(valid) == 1:
      return valid[0]
    count = 0
    for line in valid:
      count += int(line[i])
    keep = "1" if op(count,len(valid)/2) else "0"
    valid = list(filter(lambda line: line[i] == keep, valid))
  return valid[1] # special case

def part_one(readings):
  blen = len(readings[0])
  most_freq = most_common_bits(readings)
  bstr = "".join(most_freq)
  gamma = int(bstr,2)
  epsilon = 2**blen - 1 - gamma
  return gamma * epsilon

def part_two(readings):
  return int(filter_rating(readings, operator.ge),2) * int(filter_rating(readings, operator.lt),2)

def main():
  readings = process_input()
  print(part_one(readings))
  print(part_two(readings))

if __name__ == "__main__":
  main()
