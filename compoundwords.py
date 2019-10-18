import random 
import itertools
import sys
sys.setrecursionlimit(1000000000)

contents = []
compoundwordslist = []
while True:
  try:
    line = input().split(' ') 

  except EOFError:
    break
  contents.append(line)

  #selectionlist = list(range(1, 100))
  def concatanator(words_list, emptylist_compoundwords):
    landinglist = emptylist_compoundwords
    random_word1 = random.choice(words_list) 
    random_word2 = random.choice(words_list)
    if random_word1 == random_word2:
      random_word1 = random.choice(words_list) 
      random_word2 = random.choice(words_list)
    else: 
        finalcompoundword = random_word1 + random_word2
        landinglist.append(finalcompoundword)
     # the compound word cannot be a compund of itself 
    results = [' '.join(words_list[i:j]) for i, j in itertools.permutations(range(len(words_list) + 1), 2)] # limit recursion to maximum permutations  of combinations from the list 
    #remember that the maximum permutations is not what we want since the list needs to be the unique concats  
    #print("The original words are", line)
    #print("The new word list is", landinglist) ##
    if len(landinglist) <  len(results)*30: #recursion limit is 36
      concatanator(words_list, compoundwordslist)
      #if (set(landinglist)) is not len(landinglist): # check if the list is unique 
        #concatanator(words_list)
      #make the list unique 
    else:
      landinglist = list(set(landinglist))
      landinglist.sort()
      print(*landinglist, sep = "\n")
  concatanator(line, compoundwordslist)
