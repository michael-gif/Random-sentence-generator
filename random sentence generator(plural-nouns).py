import random

def determiner(nounword):
    determiner = ""
    vowels = ['a','e','i','o','u']
    vowelStart = 0
    
    if nounword[0] in vowels:
        vowelStart = True
        determiner = 'a'
    else:
        determiner = 'an'
    if vowelStart == True:
        while determiner == 'a':
          determiners = open('determiners.txt','r')
          determinerss = determiners.readlines()
          for d in range(len(determinerss)):
              determinerss[d] = determinerss[d].rstrip()
          determiner = random.choice(determinerss)
          determiners.close()
    else:    
        while determiner == 'an':
          determiners = open('determiners.txt','r')
          determinerss = determiners.readlines()
          for d in range(len(determinerss)):
              determinerss[d] = determinerss[d].rstrip()
          determiner = random.choice(determinerss)
          determiners.close()
    return determiner

def pdeterminer():
    pdeterminers = open('pdeterminers.txt','r')
    pdeterminerss = pdeterminers.readlines()
    for d in range(len(pdeterminerss)):
        pdeterminerss[d] = pdeterminerss[d].rstrip()
    pdeterminer = random.choice(pdeterminerss)
    pdeterminers.close()
    return pdeterminer

nountype = random.randint(0,1)
if nountype == 0:
  nouns = open('nouns.txt','r')
  nounss = nouns.readlines()
  for n in range(len(nounss)):
      nounss[n] = nounss[n].rstrip()
  noun = random.choice(nounss)
  nouns.close()
  nounphrase = determiner(noun) + " "
else:
  thing = ""
  nouns = open('pnouns.txt','r')
  nounss = nouns.readlines()
  for n in range(len(nounss)):
      nounss[n] = nounss[n].rstrip()
  noun = random.choice(nounss)
  nouns.close()
  choice = random.randint(0,1)
  if choice == 1:
    thing = pdeterminer() + " "
  nounphrase = thing

adjective = ""
choice = random.randint(0,1)
if choice == 1:
    adjectives = open('adjectives.txt','r')
    adjectivess = adjectives.readlines()
    for a in range(len(adjectivess)):
        adjectivess[a] = adjectivess[a].rstrip()
    adjective = random.choice(adjectivess)
    adjective += ' '
    adjectives.close()
nounphrase = nounphrase + adjective + noun

prepositionalphrase = ""
choice = random.randint(0,1)
if choice == 1:
    prepositions = open('prepositions.txt','r')
    prepositionss = prepositions.readlines()
    for p in range(len(prepositionss)):
        prepositionss[p] = prepositionss[p].rstrip()
    preposition = random.choice(prepositionss) 
    prepositions.close()
    
    nountype = random.randint(0,1)
    if nountype == 0:
      nouns = open('nouns.txt','r')
      nounss = nouns.readlines()
      for n in range(len(nounss)):
          nounss[n] = nounss[n].rstrip()
      noun = random.choice(nounss)
      nouns.close()
      nounthing = determiner(noun)
    else:
      thing = ""
      nouns = open('pnouns.txt','r')
      nounss = nouns.readlines()
      for n in range(len(nounss)):
          nounss[n] = nounss[n].rstrip()
      noun = random.choice(nounss)
      nouns.close()
      nounthing = pdeterminer()

    prepositionalphrase += ' ' + preposition + ' ' + nounthing + ' ' + noun
nounphrase += prepositionalphrase

if nountype == 0:
  verbs = open('verbs.txt','r')
  verbss = verbs.readlines()
  for v in range(len(verbss)):
      verbss[v] = verbss[v].rstrip()
  verb = random.choice(verbss)
  verbs.close()
else:
  verbs = open('pverbs.txt','r')
  verbss = verbs.readlines()
  for v in range(len(verbss)):
      verbss[v] = verbss[v].rstrip()
  verb = random.choice(verbss)
  verbs.close()
verbphrase = ' ' + verb
adverbs = open('adverbs.txt','r')
adverbss = adverbs.readlines()
for ad in range(len(adverbss)):
    adverbss[ad] = adverbss[ad].rstrip()
adverb = random.choice(adverbss)
adverbs.close()
  
verbphrase += ' ' + adverb
sentence = nounphrase + verbphrase
print(sentence)