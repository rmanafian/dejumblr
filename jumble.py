import argparse
import itertools

# Combinations implementation "inspired" by itertools.combinations
def combinations(iterable,r):
  res = []

  pool = tuple(iterable)
  n = len(pool)
  if r > n:
    return
  indices = range(r)
  res.append(''.join([pool[i] for i in indices]))
  while True:
    for i in reversed(range(r)):
      if indices[i] != i + n - r:
        break
    else:
      return res
    indices[i] += 1
    for j in range(i+1,r):
      indices[j] = indices[j-1] + 1
    res.append(''.join([pool[i] for i in indices]))

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
      wordLookup[sortedWord].append(word)
    else:
      wordLookup[sortedWord] = [word]
    words.append(line.strip().lower())

  #Skip the nC1 (single letter combinations) since they're basically useless
  #Skip nCn because that will end up being equal to sortedInput
  # This is O(n C n - 1 * n C n - 2 * ... * n C 2)*the cost of combinations
  for i in range(2,len(sortedInput)):
    for key in itertools.combinations(sortedInput,i):
      key = ''.join(key)
      if key in wordLookup:
        res.extend(wordLookup[key])

  res.extend(wordLookup[sortedInput])

  return res

parser = argparse.ArgumentParser()
parser.add_argument("input",type=str,help="Input text")
args = parser.parse_args()

print solve(args.input)
