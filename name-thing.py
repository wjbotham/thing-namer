import sys
from random import choice,randint
from string import ascii_lowercase

source = sys.argv[1]
number_of_names_to_generate = int(sys.argv[2])
f = open(source)
lines = f.readlines()
connections = { '$': list(map(lambda line: line[0], lines)) }
for line in lines:
  for i in range(len(line)-1):
    if line[i] in connections:
      connections[line[i]].append(line[i+1])
    else:
      connections[line[i]] = [line[i+1]]

for i in range(number_of_names_to_generate):
  while True:
    result = choice(connections['$'])
    while result[-1] != '\n':
      result += choice(connections[result[-1]])
    if len(result) > 2:
      break
  print(result[:-1])
