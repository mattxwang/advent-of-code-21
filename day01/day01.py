input_file = 'input.txt'

def process_input():
  with open(input_file) as f:
      content = f.readlines()
  return [int(x.strip()) for x in content]

# matt's note: these solutions fail the edge case
# if there are *very few* depths, but ... it's ok :)

def part_one(depths):
  count = 0
  for i in range(1, len(depths)):
    if depths[i-1] < depths[i]:
      count += 1
  return count

def part_two(depths):
  count = 0
  for i in range(3, len(depths)):
    if depths[i-3] < depths[i]:
      count += 1
  return count

def main():
  depths = process_input()
  print(part_one(depths))
  print(part_two(depths))

if __name__ == "__main__":
  main()
