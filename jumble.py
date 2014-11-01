import argparse

# Function to generate all combinations based on a string
# Not the most efficient, but easy to read and understand
# Each letter in the string corresponds to a binary bit
# So if the string is ABCD and the binary value is 0110
# The resulting combination is BC
# Runtime is O(2^n-1 * n)
def combinations(string):
  res = []
  fmtString = "{0:0" + str(len(string)) + "b}"
  # Start at one to skip the 'empty' combination
  for i in range(1,2 ** len(string) - 1):
    binaryArray = list(fmtString.format(i))
    resultList = [string[j] for j in range(0,len(string)) if binaryArray[j] == '1']
    res.append(''.join(resultList))

  return res

def solve(jumbledWord):
  sortedInput = ''.join(sorted(jumbledWord))

  f = open('words')
  words = []
  wordLookup = {}
  res = []

  # This is O(n) for the number of words in words.txt
  for line in f:
    word = line.strip().lower()
    sortedWord = ''.join(sorted(word))
    if sortedWord in wordLookup:
      # Skip duplicates
      if word not in wordLookup[sortedWord]:
        wordLookup[sortedWord].append(word)
    else:
      wordLookup[sortedWord] = [word]
    words.append(line.strip().lower())

  for combination in combinations(sortedInput):
    # Skip single letters because they're not very useful
    if len(combination) == 1:
      continue
    if combination in wordLookup:
      res.extend(wordLookup[combination])

  res.extend(wordLookup[sortedInput])

  return res

parser = argparse.ArgumentParser()
parser.add_argument("input",type=str,help="Input text")
args = parser.parse_args()

print solve(args.input)
