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

def sentence():
    sentence = ""
    nounphrase = ""
    verbphrase = ""
    noun = ""
    adjective = ""
    prepostion = ""
    nouns = open('nouns.txt','r')
    nounss = nouns.readlines()
    for n in range(len(nounss)):
        nounss[n] = nounss[n].rstrip()
    noun = random.choice(nounss)
    nouns.close()

    choice = random.randint(0,1)
    if choice == 1:
        adjectives = open('adjectives.txt','r')
        adjectivess = adjectives.readlines()
        for a in range(len(adjectivess)):
            adjectivess[a] = adjectivess[a].rstrip()
        adjective = random.choice(adjectivess)
        adjective += ' '
        adjectives.close()

    nounphrase += determiner(noun) + ' ' + adjective + noun

    prepositionalphrase = ""
    choice = random.randint(0,1)
    if choice == 1:
        prepositions = open('prepositions.txt','r')
        prepositionss = prepositions.readlines()
        for p in range(len(prepositionss)):
            prepositionss[p] = prepositionss[p].rstrip()
        preposition = random.choice(prepositionss)
          
        nouns = open('nouns.txt','r')
        nounss = nouns.readlines()
        for n in range(len(nounss)):
            nounss[n] = nounss[n].rstrip()
        noun = random.choice(nounss)
        nouns.close()
          
        prepositions.close()
        prepositionalphrase += ' ' + preposition + ' ' + determiner(noun) + ' ' + noun

    nounphrase += prepositionalphrase
      
    verbs = open('verbs.txt','r')
    verbss = verbs.readlines()
    for n in range(len(verbss)):
        verbss[n] = verbss[n].rstrip()
    verb = random.choice(verbss)
    verbs.close()

    verbphrase += ' ' + verb

    adverbs = open('adverbs.txt','r')
    adverbss = adverbs.readlines()
    for n in range(len(adverbss)):
        adverbss[n] = adverbss[n].rstrip()
    adverb = random.choice(adverbss)
    adverbs.close()
      
    verbphrase += ' ' + adverb
    sentence = nounphrase + verbphrase
    return sentence

run = True
while run == True:
    command = input("type 'run' or 'r' to generate a sentence. type 'exit' to close the program.\n")
    if command == "run" or command == "r":
        j = open("randomSentenceGenerator-output.txt","a")
        print("SENTENCE: " + sentence() + "\n")
        j.write("SENTENCE: " + sentence() + "\n")
        j.close()
    elif command == "exit":
        run = False
    else:
        print("invalid")
