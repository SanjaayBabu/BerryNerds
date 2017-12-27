def anagramcheck(word,checkword): 
  for letter in word:
        if letter in checkword:
          
            checkword=checkword.replace(letter, '', 1)

        else:
            return 0
  return 1

wordin=raw_input('Enter anagram:\n')



